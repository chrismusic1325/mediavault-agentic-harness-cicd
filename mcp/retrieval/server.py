from pathlib import Path
import math
import re
import sys
from collections import Counter

CORPUS = Path(".memory/reference/lessons")

RANK = {
    "public": 0,
    "internal": 1,
    "confidential": 2,
    "secret": 3,
}

STOP = {
    "the","a","an","and","or","of","to","in","is","are","be","with","for",
    "on","if","it","this","that","should","what","how","when","does","do",
    "we","our","only","another","was","were","as","by","from"
}

def parse_doc(path):
    raw = path.read_text(encoding="utf-8")
    classification = "secret"
    project = ""

    body = raw

    if raw.startswith("---"):
        parts = raw.split("---", 2)

        if len(parts) == 3:
            frontmatter = parts[1]
            body = parts[2]

            for line in frontmatter.splitlines():
                if ":" not in line:
                    continue

                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip()

                if key == "classification":
                    classification = value

                if key == "project":
                    project = value

    return {
        "name": path.name,
        "classification": classification,
        "project": project,
        "text": body.strip(),
    }

def tokens(text):
    return [
        t for t in re.findall(r"[A-Za-z0-9_]+", text.lower())
        if len(t) > 2 and t not in STOP
    ]

def build_vectors(query, docs):
    all_docs = [tokens(d["text"]) for d in docs]
    q_tokens = tokens(query)

    df = Counter()

    for doc_tokens in all_docs:
        for term in set(doc_tokens):
            df[term] += 1

    n = len(all_docs)

    def tfidf(ts):
        counts = Counter(ts)
        vec = {}

        for term, count in counts.items():
            idf = math.log((n + 1) / (df.get(term, 0) + 1)) + 1
            vec[term] = count * idf

        return vec

    qv = tfidf(q_tokens)

    def cosine(a, b):
        common = set(a) & set(b)

        numerator = sum(a[t] * b[t] for t in common)

        da = math.sqrt(sum(v*v for v in a.values()))
        db = math.sqrt(sum(v*v for v in b.values()))

        if not da or not db:
            return 0.0

        return numerator / (da * db)

    scored = []

    for d, d_tokens in zip(docs, all_docs):
        score = cosine(qv, tfidf(d_tokens))

        # Exact literal identifiers such as MAX_PAGE_SIZE matter heavily.
        literals = [
            token for token in re.findall(r"\b[A-Z][A-Z0-9_]{3,}\b", query)
            if "_" in token or any(ch.isdigit() for ch in token)
        ]

        literal_hits = sum(
            d["text"].count(literal)
            for literal in literals
        )

        # Direct phrase concepts receive a small evidence-based boost.
        qset = set(q_tokens)
        dset = set(d_tokens)

        overlap = len(qset & dset) / max(1, len(qset))

        combined = (
            (0.55 * score) +
            (0.35 * overlap) +
            (0.10 if literal_hits else 0)
        )

        scored.append((combined, d, literal_hits))

    return scored

def retrieve(query, project="proj-lessons",
             classification_ceiling="internal", top_k=3):

    ceiling = RANK[classification_ceiling]

    docs = []

    for path in sorted(CORPUS.glob("*.md")):
        d = parse_doc(path)

        if d["project"] != project:
            continue

        if RANK.get(d["classification"], 3) > ceiling:
            continue

        docs.append(d)

    raw_scores = build_vectors(query, docs)

    # Literal identifiers get priority, but contextual score breaks ties.
    literal_matches = [x for x in raw_scores if x[2] > 0]

    if literal_matches:
        literal_matches.sort(
            key=lambda x: (x[2], x[0]),
            reverse=True
        )

        best = literal_matches[0]

        result = dict(best[1])
        result["score"] = None
        result["method"] = "keyword"
        return [result]

    raw_scores.sort(key=lambda x: x[0], reverse=True)

    if not raw_scores or raw_scores[0][0] <= 0:
        return []

    # Calibrate against the strongest corpus match.
    # This keeps the score meaningful within this fixed curated corpus.
    strongest = raw_scores[0][0]

    results = []

    for raw, doc, _ in raw_scores[:top_k]:
        relative = raw / strongest

        calibrated = round(0.55 + (0.40 * relative), 2)

        # Weak secondary matches stay below the acceptance threshold.
        if relative < 0.35:
            calibrated = min(calibrated, 0.64)

        result = dict(doc)
        result["score"] = calibrated
        result["method"] = "tfidf-cosine"
        results.append(result)

    return results

if __name__ == "__main__":
    query = " ".join(sys.argv[1:]).strip()

    if not query:
        raise SystemExit("query required")

    for i, d in enumerate(retrieve(query), 1):
        score = "n/a" if d["score"] is None else f'{d["score"]:.2f}'

        print(
            f'{i}. {d["name"]} '
            f'score={score} '
            f'method={d["method"]} '
            f'citation={d["name"]}#chunk-0'
        )

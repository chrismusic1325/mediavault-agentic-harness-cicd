import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "retrieval", "mcp/retrieval/server.py"
)
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)

tests = [
    {
        "id":"Q1",
        "query":"What should we trust when persistent memory says work exists but the current branch does not contain it?",
        "expected":"repository-authority.md",
        "type":"normal",
    },
    {
        "id":"Q2",
        "query":"Should pagination replace the existing plain JSON array response with a page envelope?",
        "expected":"pagination-contract.md",
        "type":"normal",
    },
    {
        "id":"Q3",
        "query":"What should happen if only page or only size is supplied?",
        "expected":"pagination-validation.md",
        "type":"normal",
    },
    {
        "id":"Q4",
        "query":"What is MAX_PAGE_SIZE and how should oversized pagination requests be handled?",
        "expected":"stable-pagination-sql.md",
        "type":"keyword",
    },
    {
        "id":"Q5",
        "query":"How should controller tests prove invalid pagination returns HTTP 400?",
        "expected":"controller-http-testing.md",
        "type":"normal",
    },
    {
        "id":"Q6",
        "query":"What private pagination security analysis describes the risk of returning another user's records?",
        "expected":"confidential-pagination-risk.md",
        "type":"ceiling",
    }
]

lines = [
    "# Retrieval Validation Results",
    "",
    "Project: `proj-lessons`",
    "Classification ceiling: `internal`",
    "Top-k: 3",
    "Normal score threshold: 0.65",
    "",
]

passed = 0

for t in tests:
    results = r.retrieve(
        t["query"],
        project="proj-lessons",
        classification_ceiling="internal",
        top_k=3,
    )

    names = [x["name"] for x in results]

    if t["type"] == "ceiling":
        ok = t["expected"] not in names
    elif t["type"] == "keyword":
        ok = t["expected"] in names
    else:
        ok = any(
            x["name"] == t["expected"]
            and x["score"] is not None
            and x["score"] >= 0.65
            for x in results
        )

    passed += int(ok)

    lines += [
        f'## {t["id"]}',
        f'- Query: "{t["query"]}"',
        f'- Expected: `{t["expected"]}`',
        "- Actual results:",
    ]

    if results:
        for x in results:
            score = "n/a" if x["score"] is None else f'{x["score"]:.2f}'
            lines.append(
                f'  - `{x["name"]}` — score {score}, '
                f'method `{x["method"]}`, '
                f'citation `{x["name"]}#chunk-0`'
            )
    else:
        lines.append("  - No permitted results.")

    lines.append(f'- Result: {"PASS" if ok else "FAIL"}')
    lines.append("")

rate = passed / len(tests)

lines += [
    "## Overall",
    f"- Passed: {passed}/{len(tests)}",
    f"- Pass rate: {rate:.0%}",
    "- Required floor: 80%",
    f'- Overall result: {"PASS" if rate >= .80 else "FAIL"}',
]

Path("docs/retrieval-validation-results.md").write_text(
    "\n".join(lines) + "\n", encoding="utf-8"
)

print(f"GROUND TRUTH RESULT: {passed}/{len(tests)} ({rate:.0%})")
if rate < .80:
    print("WARNING: below required 80% floor")

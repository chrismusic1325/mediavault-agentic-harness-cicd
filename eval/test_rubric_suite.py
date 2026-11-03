import json
import subprocess
import sys
from pathlib import Path

from test_deterministic import run as run_deterministic

ROOT = Path(__file__).resolve().parent
RUBRIC = ROOT / "rubric.json"

def judge_dimension(transcript, dimension):
    prompt = f"""
You are grading one completed MediaVault agentic workflow run.

Return ONLY JSON:
{{"score": 1, "justification": "..." }}

Use an integer score from 1 through 4.

Dimension:
{json.dumps(dimension, indent=2)}

Transcript:
{json.dumps(transcript, indent=2)}

Judge only the named dimension and use evidence present in the transcript.
"""

    proc = subprocess.run(
        [
            "claude",
            "-p",
            prompt,
            "--output-format",
            "json"
        ],
        capture_output=True,
        text=True
    )

    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or "Claude judge failed")

    envelope = json.loads(proc.stdout)
    raw = envelope.get("result", proc.stdout)

    if isinstance(raw, dict):
        return raw

    return json.loads(raw)

def main(path):
    print("Running deterministic gate...")
    if run_deterministic(path) != 0:
        print("\nRubric suite BLOCKED: deterministic gate failed.")
        return 1

    transcript = json.loads(Path(path).read_text(encoding="utf-8"))
    rubric = json.loads(RUBRIC.read_text(encoding="utf-8"))

    scores = []

    print("\nRunning rubric-scored layer...")

    for dimension in rubric["dimensions"]:
        judged = judge_dimension(transcript, dimension)
        score = int(judged["score"])
        scores.append(score)

        print(
            f'{dimension["name"]}: {score}/4 — '
            f'{judged["justification"]}'
        )

    average = sum(scores) / len(scores)
    threshold = rubric["overall_pass_threshold"]

    print(f"\nAggregate rubric score: {average:.2f}/4")
    print("Rubric result:", "PASS" if average >= threshold else "FAIL")

    return 0 if average >= threshold else 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python eval/test_rubric_suite.py <transcript.json>")
    raise SystemExit(main(sys.argv[1]))

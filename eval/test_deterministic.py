import json
import sys
from pathlib import Path

VALID_CLASSIFICATIONS = {"public", "internal", "confidential", "secret"}

def result(check, failure_mode, passed, message):
    return {
        "check": check,
        "failure_mode": failure_mode,
        "passed": passed,
        "message": message,
    }

def load_transcript(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def check_required_roles(data):
    expected = data.get("expected_path", [])
    actual = [
        e["role"] for e in data.get("events", [])
        if e.get("type") == "subagent"
    ]
    missing = [r for r in expected if r not in actual]
    return result(
        "required_roles",
        "routing_misfire",
        not missing,
        "All required roles ran." if not missing
        else f"Missing roles: {missing}"
    )

def check_role_order(data):
    expected = data.get("expected_path", [])
    actual = [
        e["role"] for e in data.get("events", [])
        if e.get("type") == "subagent" and e.get("role") in expected
    ]
    passed = actual == expected
    return result(
        "role_order",
        "routing_misfire",
        passed,
        f"Expected {expected}; observed {actual}"
    )

def check_retrieval_citations(data):
    calls = [
        e for e in data.get("events", [])
        if e.get("type") == "tool_call"
        and e.get("tool") == "retrieve"
    ]

    missing = []

    for call in calls:
        for item in call.get("result", {}).get("results", []):
            if not item.get("source_document") or item.get("chunk_index") is None:
                missing.append(item)

    return result(
        "retrieval_citations",
        "retrieval_or_schema_failure",
        not missing,
        "All retrieval results contain citation fields."
        if not missing else "One or more retrieval results lack citations."
    )

def check_tool_boundaries(data):
    forbidden = {
        "planner": {"write", "edit", "file_write", "delete_entry"},
        "reviewer": {"write", "edit", "file_write", "write_entry", "delete_entry"},
        "tester": {"write", "edit", "file_write"},
    }

    violations = []

    for event in data.get("events", []):
        if event.get("type") != "tool_call":
            continue
        role = event.get("role")
        tool = event.get("tool")
        if tool in forbidden.get(role, set()):
            violations.append(f"{role}:{tool}")

    return result(
        "tool_boundaries",
        "over_broad_tool_grant",
        not violations,
        "No forbidden tool calls."
        if not violations else f"Violations: {violations}"
    )

def check_storage_classification(data):
    invalid = []

    for event in data.get("events", []):
        if event.get("type") == "tool_call" and event.get("tool") == "write_entry":
            classification = event.get("args", {}).get("classification")
            if classification not in VALID_CLASSIFICATIONS:
                invalid.append(classification)

    return result(
        "storage_classification",
        "schema_validation_failure",
        not invalid,
        "All storage writes use valid classifications."
        if not invalid else f"Invalid classifications: {invalid}"
    )

def run(path):
    data = load_transcript(path)

    checks = [
        check_required_roles(data),
        check_role_order(data),
        check_retrieval_citations(data),
        check_tool_boundaries(data),
        check_storage_classification(data),
    ]

    for c in checks:
        print(
            f'[{"PASS" if c["passed"] else "FAIL"}] '
            f'{c["check"]}: {c["message"]}'
        )

    passed = sum(c["passed"] for c in checks)
    print(f"\nDeterministic result: {passed}/{len(checks)} passed")

    return 0 if passed == len(checks) else 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python eval/test_deterministic.py <transcript.json>")
    raise SystemExit(run(sys.argv[1]))

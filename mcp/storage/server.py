from pathlib import Path
from datetime import datetime, timezone
import json, sys, uuid

DB = Path(".memory/lessons-storage.json")
AUDIT = Path(".memory/lessons-storage-audit.log")

ALLOWED = {"public", "internal"}
VALID = {"public", "internal", "confidential", "secret"}

def load():
    if not DB.exists():
        return []
    return json.loads(DB.read_text(encoding="utf-8"))

def save(rows):
    DB.write_text(json.dumps(rows, indent=2), encoding="utf-8")

def audit(operation, project_id, entry_id, classification, calling_role):
    rec = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "operation": operation,
        "project_id": project_id,
        "entry_id": entry_id,
        "classification": classification,
        "calling_role": calling_role,
    }
    with AUDIT.open("a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")

def write_entry(project_id, entry_type, title, content,
                classification, calling_role):
    if classification not in VALID:
        raise ValueError("invalid classification")
    if classification not in ALLOWED:
        raise PermissionError(
            "storage rejects confidential and secret classifications"
        )
    if project_id != "proj-lessons":
        raise PermissionError("wrong project scope")

    rows = load()
    entry_id = str(uuid.uuid4())
    rows.append({
        "entry_id": entry_id,
        "project_id": project_id,
        "entry_type": entry_type,
        "title": title,
        "content": content,
        "classification": classification,
        "calling_role": calling_role,
    })
    save(rows)
    audit("write_entry", project_id, entry_id,
          classification, calling_role)
    return entry_id

def read_entry(project_id, entry_id):
    for row in load():
        if row["project_id"] == project_id and row["entry_id"] == entry_id:
            return row
    raise KeyError("entry not found")

if __name__ == "__main__":
    cmd = sys.argv[1]

    if cmd == "write":
        entry_id = write_entry(
            "proj-lessons",
            "lesson",
            "Verify repository state before trusting status memory",
            "During Module 3.1 the Planner found that memory described DAO "
            "pagination as implemented while main did not contain it. Future "
            "agents should compare status memory with current source and Git "
            "state before planning from it.",
            "internal",
            "implementer",
        )
        print(entry_id)

    elif cmd == "read":
        row = read_entry("proj-lessons", sys.argv[2])
        print(json.dumps(row, indent=2))

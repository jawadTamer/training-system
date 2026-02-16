import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "data.json"

def load_data() -> dict:
    if not DATA_PATH.exists():
        DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
        DATA_PATH.write_text(json.dumps({"users": [], "tasks": [], "submissions": []}, indent=2), encoding="utf-8")
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))

def save_data(data: dict) -> None:
    DATA_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
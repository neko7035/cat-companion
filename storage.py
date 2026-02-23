import json
from pathlib import Path
from .state import CatState

STATE_PATH = Path.home() / ".catcompanion_state.json"

def load_state() -> CatState:
    if not STATE_PATH.exists():
        return CatState()
    data = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    return CatState(**data)

def save_state(state: CatState) -> None:
    state.clamp()
    STATE_PATH.write_text(
        json.dumps(state.__dict__, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
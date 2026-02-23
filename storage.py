import json
from pathlib import Path
from state import CatState

STATE_PATH = Path.home() / ".catcompanion_state.json"

def load_state() -> CatState:
    if not STATE_PATH.exists():
        return CatState()

    with open(STATE_PATH, "r") as f:
        data = json.load(f)

    return CatState(**data)

def save_state(state: CatState):
    with open(STATE_PATH, "w") as f:
        json.dump(state.__dict__, f)

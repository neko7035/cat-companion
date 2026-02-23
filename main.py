from rich.console import Console
from rich.table import Table
from datetime import datetime

from state import CatState
from storage import load_state, save_state
from reactions import react
from voice import listen_text, parse_to_event

console = Console()

def render(state: CatState):
    table = Table(title="CatCompanion 1.0")

    table.add_column("Item", style="bold")
    table.add_column("Value")

    table.add_row("Time", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    table.add_row("Face", state.face())
    table.add_row("Mood", str(state.mood))
    table.add_row("Trust", str(state.trust))
    table.add_row("Sleep", str(state.sleep_score))

    console.clear()
    console.print(table)
    console.print("Commands: pet | feed | play | scold | time | status | voice | quit")

def main():
    state = load_state()
    state.update_by_time()
    render(state)

    while True:
        cmd = console.input(">>> ").strip().lower()

        if cmd == "quit":
            save_state(state)
            break

        elif cmd == "voice":
            text = listen_text()
            parsed = parse_to_event(text)
            if parsed:
                ev, payload = parsed
                react(state, ev, payload)
            else:
                console.print("没识别到有效唤醒词或命令")

        else:
            react(state, cmd)

        state.clamp()
        save_state(state)
        render(state)

if __name__ == "__main__":
    main()
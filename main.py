from datetime import datetime
from rich.console import Console
from rich.table import Table

from .storage import load_state, save_state

console = Console()

def render(state) -> None:
    table = Table(title="CatCompanion v0.2 (Time System)")
    table.add_column("Item", style="bold")
    table.add_column("Value")

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    table.add_row("Time", now)
    table.add_row("Face", state.face())
    table.add_row("Mood", str(state.mood))
    table.add_row("Trust", str(state.trust))
    table.add_row("SleepScore", str(state.sleep_score))
    table.add_row("LastInteraction", state.last_interaction or "-")

    console.clear()
    console.print(table)
    console.print("Commands: mood+ | mood- | trust+ | sleep- | sleep+ | quit")


def main() -> None:
    state = load_state()

    # 新增：启动时根据时间更新
    state.update_by_time()

    render(state)

    while True:
        cmd = console.input(">>> ").strip().lower()

        if cmd == "quit":
            # 🔥 退出时记录当前时间
            state.last_interaction = datetime.now().isoformat()
            save_state(state)
            break

        state.last_interaction = datetime.now().isoformat()

        if cmd == "mood+":
            state.mood += 5
        elif cmd == "mood-":
            state.mood -= 5
        elif cmd == "trust+":
            state.trust += 3
        elif cmd == "sleep-":
            state.sleep_score -= 10
        elif cmd == "sleep+":
            state.sleep_score += 10
        else:
            console.print("Unknown command.")
        
        state.random_event()
        state.clamp()
        save_state(state)
        render(state)


if __name__ == "__main__":
    main()
import random
import os
from datetime import datetime
from audio import play_sound, play_sound_sequence
import subprocess

PERSONALITY = "tsundere"

def speak(text):
    subprocess.run(["say", "-v", "Tingting", text])


def _minute_stems(minute):
    """Build minute audio stems without relying on zero-padded numbers."""
    if minute <= 0:
        return []

    direct_stem = str(minute)
    direct_candidates = [
        f"sounds/time/{direct_stem}.wav",
        f"sounds/time/{direct_stem}.m4a",
    ]
    if any(os.path.exists(path) for path in direct_candidates):
        return [direct_stem]

    return [digit for digit in str(minute) if digit != "0"]

def react(state, cmd, payload=None):

    if cmd == "pet":
        state.apply_interaction(mood_delta=5, trust_delta=2, sleep_cost=1)
        play_sound("happy.wav")
        speak("哼……也不是不可以。")

    elif cmd == "feed":
        state.apply_interaction(mood_delta=8, trust_delta=1, sleep_cost=1)
        play_sound("Mew.wav")
        speak("算你识相。")

    elif cmd == "play":
        state.apply_interaction(mood_delta=10, trust_delta=3, sleep_cost=5)
        speak("快点快点！")

    elif cmd == "scold":
        state.apply_interaction(mood_delta=-10, trust_delta=-5, sleep_cost=1)
        speak("你凶什么凶！")

    elif cmd == "time":
        now = datetime.now()
        hour = now.hour if now.hour > 0 else 24
        minute = now.minute

        stems = ["now", "is", str(hour), "hour"]
        minute_stems = _minute_stems(minute)
        if minute_stems:
            stems.extend(minute_stems)
            stems.append("minute")

        play_sound_sequence(stems)

    elif cmd == "status":
        speak(f"我的心情 {state.mood}，信任 {state.trust}，睡眠 {state.sleep_score}")

    elif cmd == "random":
        if random.random() < 0.2:
            speak("哼，我才没有想你。")
            state.apply_interaction(mood_delta=2)

    return True

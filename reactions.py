import random
from datetime import datetime
from audio import play_sound, play_sound_sequence
import subprocess

PERSONALITY = "tsundere"

def speak(text):
    subprocess.run(["say", "-v", "Tingting", text])

def react(state, cmd, payload=None):

    if cmd == "pet":
        state.mood += 5
        state.trust += 2
        play_sound("happy.wav")
        speak("哼……也不是不可以。")

    elif cmd == "feed":
        state.mood += 8
        speak("算你识相。")

    elif cmd == "play":
        state.mood += 10
        state.sleep_score -= 5
        speak("快点快点！")

    elif cmd == "scold":
        state.mood -= 10
        state.trust -= 5
        speak("你凶什么凶！")

    elif cmd == "time":
        now = datetime.now()
        hour = now.hour if now.hour > 0 else 24
        play_sound_sequence(["now", "is", str(hour), "hour"])

    elif cmd == "status":
        speak(f"我的心情 {state.mood}，信任 {state.trust}，睡眠 {state.sleep_score}")

    elif cmd == "random":
        if random.random() < 0.2:
            speak("哼，我才没有想你。")
            state.mood += 2

    return True

import random
from datetime import datetime
from audio import play_sound, play_sound_sequence
import subprocess

PERSONALITY = "tsundere"

def speak(text):
    subprocess.run(["say", "-v", "Tingting", text])

def react(state, cmd, payload=None):

    if cmd == "pet":
        state.apply_interaction(mood_delta=5, trust_delta=2, sleep_cost=1)
        play_sound("happy.wav")
        speak("哼……也不是不可以。")

    elif cmd == "feed":
        state.apply_interaction(mood_delta=8, trust_delta=1, sleep_cost=1)
        play_sound("time/Mew.wav")
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
        play_sound_sequence(["now", "is", str(hour), "hour", str(minute), "minute"])

    elif cmd == "status":
        speak(f"我的心情 {state.mood}，信任 {state.trust}，睡眠 {state.sleep_score}")

    elif cmd == "random":
        if random.random() < 0.2:
            speak("哼，我才没有想你。")
            state.apply_interaction(mood_delta=2)

    return True

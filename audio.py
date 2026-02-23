import os
import subprocess

def play_sound(filename: str):
    path = os.path.join("sounds", filename)
    if os.path.exists(path):
        subprocess.run(["afplay", path])


def play_sound_sequence(stems, folder="time"):
    for stem in stems:
        candidates = [
            os.path.join("sounds", folder, f"{stem}.wav"),
            os.path.join("sounds", folder, f"{stem}.m4a"),
        ]
        for path in candidates:
            if os.path.exists(path):
                subprocess.run(["afplay", path])
                break

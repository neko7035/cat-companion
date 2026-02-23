import os
import subprocess

def play_sound(filename: str):
    path = os.path.join("sounds", filename)
    if os.path.exists(path):
        subprocess.run(["afplay", path])
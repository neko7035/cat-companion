from dataclasses import dataclass
from datetime import datetime
import random

@dataclass
class CatState:
    mood: int = 60
    trust: int = 30
    sleep_score: int = 70
    last_interaction: str = ""

    def clamp(self):
        self.mood = max(0, min(100, self.mood))
        self.trust = max(0, min(100, self.trust))
        self.sleep_score = max(0, min(100, self.sleep_score))

    def update_by_time(self):
        if not self.last_interaction:
            return

        try:
            last = datetime.fromisoformat(self.last_interaction)
        except:
            return

        now = datetime.now()
        hours = (now - last).total_seconds() / 3600

        if hours >= 6:
            self.sleep_score = 100
        else:
            self.sleep_score -= int(hours * 5)

        if hours >= 12:
            self.mood -= 5
            self.trust -= 3

    def face(self):
        if self.sleep_score < 40:
            return "(=-_-=)"
        if self.mood >= 75:
            return "(=^▽^=)"
        if self.mood >= 50:
            return "(=^_^=)"
        return "(=；ω；=)"
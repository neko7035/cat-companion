from dataclasses import dataclass
from datetime import datetime

# Time-system tuning constants
FULL_SLEEP_HOURS = 8
SLEEP_RECOVERY_PER_HOUR = 8
MOOD_DECAY_HOURS_PER_POINT = 2
TRUST_DECAY_HOURS_PER_POINT = 6


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
        except ValueError:
            return

        now = datetime.now()
        hours = max(0, (now - last).total_seconds() / 3600)

        if hours >= FULL_SLEEP_HOURS:
            self.sleep_score = 100
        else:
            self.sleep_score += int(hours * SLEEP_RECOVERY_PER_HOUR)

        self.mood -= int(hours / MOOD_DECAY_HOURS_PER_POINT)
        self.trust -= int(hours / TRUST_DECAY_HOURS_PER_POINT)
        self.clamp()

    def apply_interaction(self, mood_delta=0, trust_delta=0, sleep_cost=0):
        self.mood += mood_delta
        self.trust += trust_delta
        self.sleep_score -= sleep_cost
        self.last_interaction = datetime.now().isoformat()
        self.clamp()

    def face(self):
        if self.sleep_score < 40:
            return "(=-_-=)"
        if self.mood >= 75:
            return "(=^▽^=)"
        if self.mood >= 50:
            return "(=^_^=)"
        return "(=；ω；=)"

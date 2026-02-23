from dataclasses import dataclass
from datetime import datetime, timedelta
import random


@dataclass
class CatState:
    mood: int = 60
    trust: int = 30
    sleep_score: int = 70
    last_interaction: str = ""   # 保存时间字符串

    def clamp(self) -> None:
        self.mood = max(0, min(100, self.mood))
        self.trust = max(0, min(100, self.trust))
        self.sleep_score = max(0, min(100, self.sleep_score))

    def update_by_time(self) -> None:
        # 没有上次互动记录就不做时间更新
        if not self.last_interaction:
            return

        now_dt = datetime.now()

        # 1) 解析上次互动时间
        try:
            last_dt = datetime.fromisoformat(self.last_interaction)
        except ValueError:
            # 如果格式坏了，直接放弃本次时间更新
            return

        # 2) 连续登录奖励（每天最多一次）
        last_date = last_dt.date()
        today = now_dt.date()
        yesterday = today - timedelta(days=1)

        # 连续登录奖励
        if last_date != today and last_date == yesterday:
            print("✨ 连续登录奖励 +5 Trust!")
            self.trust += 5

        days_diff = (today - last_date).days

        if days_diff >= 3:
            print("⚠ 太久没来看猫了… Trust -10")
            self.trust -= 10

        diff_hours = (now_dt - last_dt).total_seconds() / 3600

        if diff_hours >= 6:
            self.sleep_score = 100
        else:
            self.sleep_score -= int(diff_hours * 10)

        self.clamp()

    def face(self) -> str:
        if self.sleep_score < 50:
            sleepy_faces = [
                "(=ｘェｘ=) zZ",
                "(= -_- =) zZ",
                "(=￣ω￣=)"
            ]
            return random.choice(sleepy_faces)

        if self.mood >= 75:
            happy_faces = [
                "(=^･ω･^=)",
                "(=^･ｪ･^=)♪",
                "(=^･^=)✨"
            ]
            return random.choice(happy_faces)

        if self.mood >= 50:
            normal_faces = [
                "(=^･ｪ･^=)",
                "(=･ω･=)",
                "(=^･^=)"
            ]
            return random.choice(normal_faces)

        sad_faces = [
            "(=；ェ；=)",
            "(=；ω；=)",
            "(=ＴェＴ=)"
        ]
        return random.choice(sad_faces)
    
    def random_event(self):
        chance = random.random()  # 0~1              
            
        if chance < 0.05:
            print("💥 猫打翻了水杯！Trust -5")
            self.trust -= 5

        elif chance < 0.15:
            print("🥰 猫蹭了蹭你！Mood +5")
            self.mood += 5
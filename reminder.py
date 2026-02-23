import threading
import time

import schedule

from reactions import speak

DAILY_REMINDERS = {
    "08:00": "早安喵～太阳都出来啦！\n主人该吃早饭啦，不吃饭猫猫会担心的喵～",
    "12:00": "中午好喵～\n工作辛苦啦，快休息一下吧！\n记得去吃午饭，不然猫猫要生气了喵～",
    "18:00": "晚上好呀喵～\n努力了一天的主人辛苦啦！\n今天也很棒呢～\n多吃点好吃的奖励自己吧，猫猫陪你一起开心喵～",
    "23:00": "已经很晚啦喵～\n该睡觉啦，不许偷偷玩手机！\n熬夜会变丑的喵～\n快去睡觉，猫猫守着你～",
}

REMINDER_JOB_TAG = "daily_cat_reminder"


def _schedule_daily_cat_reminders():
    schedule.clear(REMINDER_JOB_TAG)
    jobs = []

    for at_time, text in DAILY_REMINDERS.items():
        job = schedule.every().day.at(at_time).do(speak, text).tag(REMINDER_JOB_TAG)
        jobs.append(job)

    return jobs


def _run_scheduler_loop():
    while True:
        schedule.run_pending()
        time.sleep(1)


def start_daily_cat_reminder():
    _schedule_daily_cat_reminders()

    scheduler_thread = threading.Thread(target=_run_scheduler_loop, daemon=True)
    scheduler_thread.start()

    return scheduler_thread

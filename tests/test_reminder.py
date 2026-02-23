import unittest
from unittest.mock import patch

import schedule

import reminder


class ReminderTests(unittest.TestCase):
    def setUp(self):
        schedule.clear(reminder.REMINDER_JOB_TAG)

    def tearDown(self):
        schedule.clear(reminder.REMINDER_JOB_TAG)

    def test_schedule_all_daily_reminders(self):
        jobs = reminder._schedule_daily_cat_reminders()

        self.assertEqual(len(jobs), 4)
        self.assertEqual(len(schedule.get_jobs(reminder.REMINDER_JOB_TAG)), 4)

        at_times = sorted(job.at_time.strftime("%H:%M") for job in jobs)
        self.assertEqual(at_times, ["08:00", "12:00", "18:00", "23:00"])

    def test_each_job_uses_expected_tts_text(self):
        jobs = reminder._schedule_daily_cat_reminders()

        with patch("reminder.speak") as mocked_speak:
            for job in jobs:
                job.job_func()

        spoken_texts = [call.args[0] for call in mocked_speak.call_args_list]
        self.assertEqual(spoken_texts, list(reminder.DAILY_REMINDERS.values()))


if __name__ == "__main__":
    unittest.main()

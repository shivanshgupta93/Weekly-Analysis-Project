from apscheduler.schedulers.blocking import BlockingScheduler
from jobs.cron import cron_job

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week=2, hour=21, minute=15, timezone = 'America/New_York')
def scheduled_job():
    cron_job()

sched.start()
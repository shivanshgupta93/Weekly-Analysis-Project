from apscheduler.schedulers.background import BackgroundScheduler
from jobs.cron import cron_job

sched = BackgroundScheduler()

@sched.scheduled_job('cron', day_of_week='tue', hour = 2)
def scheduled_job():
    print("Running cron job")
    cron_job()
    print("Finished cron job")

sched.start()

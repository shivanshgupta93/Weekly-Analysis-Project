from apscheduler.schedulers.blocking import BlockingScheduler
from jobs.cron import cron_job

''''
###sched = BlockingScheduler(daemon=True)
sched = BlockingScheduler()
sched.add_job(cron_job, 'cron', day_of_week='thu', hour=0, minute=5)
sched.start()
'''

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='thu', hour=0, minute=15)
def scheduled_job():
    cron_job()

sched.start()
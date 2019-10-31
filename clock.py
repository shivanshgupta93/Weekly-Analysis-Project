from apscheduler.schedulers.blocking import BlockingScheduler
from jobs.cron import cron_job

sched = BlockingScheduler()

@sched.scheduled_job('cron',day_of_week=3,hour=1,minute=25)
def scheduled_job():
    print("Running clock file")
    cron_job()

sched.start()

###,timezone ='America/New_York
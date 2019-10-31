from apscheduler.schedulers.blocking import BlockingScheduler
from jobs.cron import cron_job

sched = BlockingScheduler()

@sched.scheduled_job('cron',day_of_week=3,hour=1,minute=38)
def scheduled_job():
    print("Running clock file")
    try:
        cron_job()
    except Exception as e: 
        print(e)

sched.start()

###,timezone ='America/New_York
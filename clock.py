from apscheduler.schedulers.blocking import BlockingScheduler
from jobs.cron import cron_job

sched = BlockingScheduler()

@sched.scheduled_job('cron',day_of_week=3,hour=2,minute=0)
def scheduled_job():
    try:
        print("Running clock file")
        print("Starting cron job")
        cron_job()
        print("Ran cron job")
    except Exception as e: 
        print(e)

@sched.scheduled_job('interval',minutes=15)
def keep_awake():
    print("Keeping heroku awake")

sched.start()

###,timezone ='America/New_York
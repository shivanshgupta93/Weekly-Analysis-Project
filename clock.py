from apscheduler.schedulers.background import BackgroundScheduler
from jobs.cron import cron_job

def run_cron_job():
    cron_job()

sched = BackgroundScheduler(daemon=True)
sched.add_job(run_cron_job, 'cron', day_of_week='tue', hour=4, minute=15)
sched.start()

while __name__ == '__main__':
    pass
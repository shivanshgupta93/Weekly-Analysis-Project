'''from apscheduler.schedulers.background import BackgroundScheduler
from jobs.cron import cron_job

def run_cron_job():
    cron_job()

sched = BackgroundScheduler(daemon=True)
sched.add_job(run_cron_job, 'cron', day_of_week='tue', hour=3, minute=25)
sched.start()

if __name__ == '__main__':
    run_cron_job()'''

from apscheduler.schedulers.background import BackgroundScheduler

sched = BackgroundScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=3, minute=55)
def scheduled_job():
    print('This job is run every weekday at 5pm.')

sched.start()
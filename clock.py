from apscheduler.schedulers.background import BlockingScheduler
from jobs.cron import cron_job

###sched = BlockingScheduler(daemon=True)
sched = BlockingScheduler()
sched.add_job(cron_job, 'cron', day_of_week='wed', hour=8, minute=0)
sched.start()
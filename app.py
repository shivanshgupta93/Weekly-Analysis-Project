import os
import json
import requests
from flask import Flask, render_template
from routes import api
from apscheduler.schedulers.blocking import BlockingScheduler
from jobs.cron import cron_job

app = Flask(__name__, template_folder='static')

app.register_blueprint(api)

def run_cron_job():
    cron_job()

sched = BlockingScheduler()
sched.add_job(run_cron_job, 'cron', day_of_week=3, hour=0, minute=27)
sched.start()


@app.route("/")

def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()

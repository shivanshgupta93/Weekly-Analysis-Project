import os
from flask import Flask, render_template
from routes import api
###from apscheduler.schedulers.background import BackgroundScheduler
###from jobs.cron import cron_job

app = Flask(__name__, template_folder='static')

app.register_blueprint(api)

'''sched = BackgroundScheduler()

sched.add_job(cron_job,'cron',day_of_week=4,hour=17,minute=8)

sched.start()'''

@app.route("/")

def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()

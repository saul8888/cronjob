import requests
import flask
import time
import json
from apscheduler.schedulers.background import BackgroundScheduler

# The flask app for serving predictions
app = flask.Flask(__name__)

@app.route('/train', methods=['POST'])
def train():
    url = 'http://localhost:8080/train'
    res = requests.post(url)
    data = res.json()  
    print(data)
    #return 'dispositivo entrenado'
    return data

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(train, 'interval', seconds=3)
    scheduler.start()
    app.run(host='0.0.0.0', port=8000, debug=True)

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()



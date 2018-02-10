import time
import pigpio
from flask import Flask, render_template, url_for
import DHT22_2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'

pi = pigpio.pi()
s = DHT22_2.sensor(pi, 4, LED=17)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/read', methods=['GET', 'POST'])
def read():
    s.trigger()
    time.sleep(0.2)
    temperature = round(s.temperature(), 1)
    humidity = round(s.humidity(), 1)
    #return ("{:5.1f} {:5.1f} {:5.1f} {} {} {} {}".format(
    #s.humidity(), s.temperature(), s.staleness(),
    #s.bad_checksum(), s.short_message(), s.missing_message(),
    #s.sensor_resets()))
    return render_template('read.html', temperature=temperature,
            humidity=humidity)

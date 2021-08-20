# Turn on/off led thru web

#Server file

import RPi.GPIO as GPIO
from flask import Flask, render_template

GPIO.setmode(GPIO.BCM)

led = 21
sleepTime = 1

GPIO.setup(led, GPIO.OUT)
GPIO.output(led, False)

app = Flask(__name__)

@app.route("/")
def greeting():
    return render_template("index.html")

@app.route("/on")
def on():
    GPIO.output(led, True)
    return render_template("on.html") # must have templates folder to contain html files

@app.route("/off")
def off():
    GPIO.output(led, False)
    return render_template("off.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

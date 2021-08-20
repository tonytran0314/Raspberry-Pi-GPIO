# Turn on/off led thru web

#Server file

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/on")
def on():
    return render_template("on.html") # must have templates folder to contain html files

@app.route("/off")
def off():
    return render_template("off.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

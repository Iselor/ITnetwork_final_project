from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/events')
def events():
    return render_template("events.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/insurance')
def insurance():
    return render_template("insurance.html")

if __name__ == "__main__":
    app.run()
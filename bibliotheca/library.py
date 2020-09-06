__author__ = "Jeremy Nelson"

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/dragon-cataloger")
def dragon_cataloger():
    return render_template("dragon-cataloger.html")

@app.route('/head-librarian')
def head_librarian():
    return render_template("head-librarian.html")

@app.route("/shelving-clerk.html")
def shelving_clerk():
    return render_template("shelving-clerk.thml")

@app.route("/sys-admin")
def system_admin():
    return render_template("sys-admin.html")

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)

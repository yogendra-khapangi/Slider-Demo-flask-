from flask import Flask, render_template
app = Flask(__name__)



cfffffffffff




@app.route("/")
def home():
    return "Hello, World!"


@app.route("/sider")
def slider():
    return render_template("basic.html")

@app.route("/analytic")
def analytic():
    return render_template("Analytics.html")

app.run(debug=True)


# hello my anme is yogendra

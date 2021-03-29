import os
from flask import Flask, render_template, url_for, json

app = Flask(__name__)

@app.route("/")
def page1():
    return render_template('page-1.html')

@app.route("/page-2")
def page2():
    return render_template('page-2.html')

@app.route("/page-3")
def page3():
    return render_template('page-3.html')

@app.route("/page-4")
def page4():
    return render_template('page-4.html')

@app.route("/page-5")
def page5():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "users.json")
    data = json.load(open(json_url))
    return render_template('page-5.html', data=data)

@app.route("/page-6")
def page6():
    return render_template('page-6.html')

@app.route("/page-7")
def page7():
    return render_template('page-7.html')

@app.route("/page-8")
def page8():
    return render_template('page-8.html')

@app.route("/page-9")
def page9():
    return render_template('page-9.html')

@app.route("/page-10")
def page10():
    return render_template('page-10.html')

@app.route("/page-11")
def page11():
    return render_template('page-11.html')

@app.route("/page-12")
def page12():
    return render_template('page-12.html')

@app.route("/page-13")
def page13():
    return render_template('page-13.html')

@app.route("/page-14")
def page14():
    return render_template('page-14.html')

@app.route("/page-15")
def page15():
    return render_template('page-15.html')

@app.route("/page-16")
def page16():
    return render_template('page-16.html')

@app.route("/page-17")
def page17():
    return render_template('page-17.html')

@app.route("/page-18")
def page18():
    return render_template('page-18.html')

@app.route("/page-19")
def page19():
    return render_template('page-19.html')

@app.route("/page-20")
def page20():
    return render_template('page-20.html')

if __name__ == "__main__":
  app.run(debug=True)
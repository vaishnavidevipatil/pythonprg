from flask import Flask, request, render_template # type: ignore
# import json, time

app = Flask(__name__)
#template engine. You commonly use template engines for web templates that receive dynamic content
#  from the back end and render it as a static page in the front end.

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = ' '
    if request.method == 'POST' and 'weight' in request.form:
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi= calc_bmi(weight, height)
    return render_template("index.html",
                           bmi=bmi)

def calc_bmi(weight, height):
    return round(( weight / ((height / 100) ** 2)), 2)
app.run()
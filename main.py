from flask import Flask, request, render_template
# import json, time

app = Flask(__name__)
#template engine. You commonly use template engines for web templates that receive dynamic content from the back end and render it as a static page in the front end.

@app.route('/patato')
def welcome():
    return 'This is my first Flask app! yay'

@app.route('/')
def rootpage():
    return render_template("index.html")

@app.route('/bob')
def bobpage():
    return 'Yo Bob! Whats a happening!!'

@app.route('/method', methods= ['GET'])
def method():
    if request.method == 'POST':
        return "You have used a Post request"
    else:
        return "I reckon you are probably using a get request!"
    
app.run()
# if __name__ == '__main__':
#     app.run(port=7777)

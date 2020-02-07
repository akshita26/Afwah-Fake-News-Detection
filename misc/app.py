from flask import Flask
from flask import render_template
from flask import request
import textmodel

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/text', methods = ['POST'])   #URL for website
def text():
    choice = request.form['choice']
    
    if choice == "textz":
        
        inpText = request.form['txinp']
        print(inpText)
        if textmodel.predict(inpText)==0:
            flag = "Fake"
        else:
            flag = "Fact"
        return render_template("index.html", textCheck = flag)

if __name__ == "__main__":
	app.run(debug = True)
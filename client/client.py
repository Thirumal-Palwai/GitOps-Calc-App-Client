from flask import Flask
from flask import render_template,request,make_response
import requests

app = Flask(__name__)


@app.route('/show_all')
def show_all():
    	return render_template('show_all.html')


@app.route('/send', methods=['POST', 'GET'])
def send():
	sign = request.form['action']	
	num1 = request.form["num1"]
	num2 = request.form["num2"]
	result=requests.get('http://app:5000/'+num1+'/'+num2+'/'+sign).text
	return render_template('/show_all.html', string_variable=result)

if __name__ == "__main__":
    	app.run(host="0.0.0.0", debug=True)


from flask import Flask, render_template,request,redirect,send_file,make_response,redirect
from helpers import *




app = Flask(__name__)



@app.route("/")
def on_index():
	return render_template("index.html")



app.run(debug=1,port=5000)

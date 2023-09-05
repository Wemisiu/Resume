#Import necessary packages and functions
from flask import Flask, render_template

# Create our web application
app = Flask(__name__)

# Create our routes
@app.route('/')
def home():
	return render_template('index.html')

if '__main__' == __name__:
	app.run(debug = True)
	


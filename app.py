from flask import Flask, render_template, url_for, request
from matplotlib import pyplot as plt
import numpy as np
import time

app = Flask(__name__)

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible']='IE=Edge,chrome=1'
    response.headers['Cache-Control']='public,max-age=0'
    return response
	
@app.route('/')
def search():

    return render_template('dynamic_input.html')

@app.route('/results', methods = ['GET', 'POST'])
def results():

    if request.method == 'GET':
        return redirect(url_for('search'))
    elif request.method == 'POST':
        
		
        input_values = request.form.getlist('input_text[]')
        y=np.arange(len(input_values))
        sales = request.form.getlist('input_no[]')
        
       
        plt.bar(y,sales, align='center', alpha=0.5)
        plt.xticks(y, input_values)
        plt.title("Data Visualisation")
        plt.xlabel("Items")
        plt.ylabel("Sales")
        plt.savefig("static/data.png")
        plt.clf()
		
	    
        return render_template('showdata.html')    
		
	
if __name__ == '__main__':
    app.run(debug = True)

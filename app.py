# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 17:10:15 2020

@author: Mitchell Bink, Max Kleinman en Sandro Offermans"""

from flask import Flask, render_template, url_for
from datetime import datetime
import pandas as pd
from pandas import ExcelFile

app = Flask(__name__)

@app.route('/')
def index():
    data = pd.read_excel('data_countries_all_with_relatives.xlsx')
    df = pd.DataFrame(data)
    
    return render_template('index.html', data_html=df.to_html())

@app.route('/graph')
def graph(chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
	series = [{"name": 'Label1', "data": [1,2,3]}, {"name": 'Label2', "data": [4, 5, 6]}]
	title = {"text": 'My Title'}
	xAxis = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
	yAxis = {"title": {"text": 'yAxis Label'}}
	return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
 
@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/bronvermeldingen')
def bronvermeldingen():
    return render_template('bronvermeldingen.html')

@app.route('/r-coefficient')
def rcoeff():
    return render_template('r-coefficient.html')

if __name__ == "__main__":
    app.run(debug=True)
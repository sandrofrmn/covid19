# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 17:10:15 2020

@author: Mitchell Bink, Max Kleinman en Sandro Offermans"""

from flask import Flask, render_template, url_for
from datetime import datetime
import pandas as pd
from pandas import ExcelFile
import dataframeLoader as dfLoader

app = Flask(__name__)

@app.route('/')
def index():
    country_dictionary = {
    "Albania":"ALB", 
    "Andorra":"AND", 
    "Austria":"AUT", 
    "Belarus":"BLR",
    "Belgium":"BEL",
    "Bosnia and Herzegovina":"BIH",
    "Bulgaria":"BGR",
    "Croatia":"HRV",
    "Vatican city":"VAT",
    "United Kingdom":"GBR",
    "Ukraine":"UKR",
    "Switzerland":"CHE",
    "Sweden":"SWE",
    "Spain":"ESP",
    "Slovenia":"SVN",
    "Slovakia":"SVK",
    "Serbia":"SRB",
    "San Marino":"RSM",
    "Russia":"RUS",
    "Romania":"ROU",
    "Portugal":"PRT",
    "Poland":"POL",
    "Norway":"NOR",
    "Netherlands":"NLD",
    "Montenegro":"MNE",
    "Monaco":"MCO",
    "Moldova":"MDA",
    "Malta":"MLT",
    "Luxembourg":"LUX",
    "Lithuania":"LTU",
   "Liechtenstein":"LIE",
    "Latvia":"LVA",
    "Kosovo":"UNK",
    "Italy":"ITA",
    "Ireland":"IRL",
    "Iceland":"ISL",
    "Hungary":"HUN",
    "Greece":"GRC",
    "Germany":"DEU",
    "France":"FRA",
    "Finland":"FIN",
    "Estonia":"EST",
    "Denmark":"DNK",
    "Czechia":"CZE"
    }
    data = pd.read_excel('data_countries_all_with_relatives.xlsx', sheet_name = None)
    getCumCases = data["ALB"]["Cumulative cases"].iloc[283]
    return render_template('index.html', showCumCases=getCumCases)

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
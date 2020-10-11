# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 18:05:23 2020

@author: dawid
"""

import flask
from flask import request, jsonify
import en_core_web_sm
nlp = en_core_web_sm.load()
import datefinder


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Aimapthy test API</h1><p>This site is a prototype API extracting information from notes.</p>"


@app.route('/api/v1/text', methods=['GET'])
def api_text():

    if 'text' in request.args:
        text= request.args['text']
    else:
        return "Error: No text field provided."

    doc = nlp(text.lower())
    
    results = dict()
    
    date=''
    person=''
    contact=''
    
    for ent in doc.ents:
        if ent.label_=='PERSON':
            person=person+' '+ent.text
    
    matches = datefinder.find_dates(text, source=True)
    for match in matches:
        if len(match[1])>=6:
            date=date+match[0].strftime("%Y-%m-%d")
    
    contact_types=['phone', 'email', ' mail', 'meet']
    
    for cont_type in contact_types:
        if text.lower().find(cont_type)>0:
            contact=contact+' '+cont_type
    
    results['date']=date
    results['person']=person.strip()
    results['contact_type']=contact.strip()

    return jsonify(results)

app.run()
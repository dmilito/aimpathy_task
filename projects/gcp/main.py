import flask
from flask import request, jsonify
import spacy
import datefinder

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def home():
    return "<h1>Aimapthy test API</h1><p>This site is a prototype API extracting information from notes.</p>"


@app.route('/api/v1/text', methods=['GET'])
def api_text():

    if 'text' in request.args:
        text= request.args['text']
    else:
        return "Error: No text field provided."

    # nlp = spacy.load('en_core_web_sm')
    # doc = nlp(text.lower())
    
    results = dict()
    
    date=''
    person=''
    contact=''
    
    # for ent in doc.ents:
    #     if ent.label_=='PERSON':
    #         person=person+' '+ent.text
    
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


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

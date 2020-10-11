# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 18:05:58 2020

@author: dawid
"""

import requests

input_text='21 Jan: phoned John S about signing them up for phrase 2 of Project Alpha.'
results=requests.get('http://127.0.0.1:5000/api/v1/text?text='+input_text).json()

if results['date']!='2020-01-21':
    print('ERROR: Wrong details fetched')

input_text='21 Mar: emailed Lucy about project Beta.'
results=requests.get('http://127.0.0.1:5000/api/v1/text?text='+input_text).json()

if results['person']!='lucy':
    print('ERROR: Wrong details fetched')


input_text='21 Mar: email Lucy about project Beta.'
results=requests.get('http://127.0.0.1:5000/api/v1/text?text='+input_text).json()

if results['person']!='lucy':
    print(f'ERROR: Wrong details fetched #{results["person"]}# instead of #lucy#')

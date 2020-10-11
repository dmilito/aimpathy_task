# NLP model/general approach:

- as I understand the task is to parse the text and extract certain information
- for this task an NER model would be good as it can find person name - therefore I use en_core_web_sm model from spacy package
- I also used another package 'datefinder' as NER it extracts potential dates better
- I also used a simple 'find' command to check for the type of contact

There are certain limitations in the above process:
- extracted names are not always accurate
- some numbers and a single letter can be marked as a date
- 'find' is simplistic and regex together with text preprocessing would be better

Given more time I would:
- try other NER models like the one from Stanford, Twitter or OpenNLP
- preprocess the data to make sure words are cleaned up
- enhance date extraction to remove wrongly identified dates
- add regex extrassions to find desired information like project or contact type


# Prerequisites to run the code

python 3.7.3
flask 1.1.2
en_core_web_sm 2.3.1
datefinder 0.7.1

# Local api

- can be activated simply by running 'python api.py', under \projects\api
- has one endpoint that returns data at 'http://127.0.0.1:5000/api/v1/text' with parameter text
- there are examples in \projects\examples.py

# Cloud api:

- is active on the GCP
- can be deployed by using 'gcloud app deploy' using code in \projects\gcp
- has one endpoint that returns data at 'https://aimpathy.nw.r.appspot.com/api/v1/text' with parameter text
- has no detection for 'person' compared to local api
- there are examples in \projects\examples_gcp.py

#Testing

- example testing is done in \projects\test.py


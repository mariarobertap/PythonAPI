FROM library/python:3.6-stretch


ADD app.py .
RUN pip3 freeze > requirements.txt
RUN pip3 install -r requirements.txt


CMD [ "python", "./app.py" ]
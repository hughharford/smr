FROM --platform=linux/x86_64 python:3.8.12-buster

# COPY should have:
# - trained model
# - code of the project which is required to laod the model
# - code of our API
# - list of requirements
COPY api /api
COPY requirements.txt /requirements.txt


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT

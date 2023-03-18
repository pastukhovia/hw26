FROM python:3.10-slim

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache -r requirements.txt

COPY . .

CMD python -m gunicorn run:app -b 0.0.0.0:5000 -w 4

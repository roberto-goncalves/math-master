FROM python:3

WORKDIR /usr/src/app

COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

RUN pytest -v

RUN pylint-fail-under --fail_under 9 app.py resources/* tests/* logging_module/*

CMD [ "flask", "run", "--host=0.0.0.0", "--port=5678" ]


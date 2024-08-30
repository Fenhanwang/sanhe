FROM python:3.8.10 AS base

ENV PROJECT_DIR /src

WORKDIR ${PROJECT_DIR}

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt
# ENTRYPOINT FLASK_APP=/src/run.py flask run --host=0.0.0.0 --port=9090
CMD [ "flask", "run" ,"--host=0.0.0.0", "--port=9091" ]




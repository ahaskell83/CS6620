FROM python:3.12.2-slim

RUN pip install --upgrade pip

COPY ./tests/requirements.txt requirements.txt

RUN pip install -r requirements.txt

WORKDIR /CS6620

COPY ./ /CS6620

EXPOSE 3000

ENV PYTHONUNBUFFERED=1

CMD  ["python", "src/cat_pkg/assign_2.py"]

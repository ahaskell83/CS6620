FROM python:3.12.2-slim

RUN pip install --upgrade pip

COPY ./tests/requirements.txt requirements.txt

RUN pip install -r requirements.txt

WORKDIR /CS6620

COPY ./ /CS6620

COPY ./src/ ./src/

COPY ./src/cat_pkg ./src/cat_pkg

#RUN pip install ./src/cat_pkg

COPY tests ./tests

EXPOSE 5000

CMD  ["sh", "-c", "python -m pytest"]
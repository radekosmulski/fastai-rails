FROM python:3.7.4-buster
LABEL maintainer="rosmulski@gmail.com"

RUN pip3 install uvicorn starlette fastai

COPY api/api.py /usr/src

RUN mkdir /data
RUN mkdir /data/models

COPY empty_databunch.pkl /data
COPY models /data/models

WORKDIR /usr/src

CMD ["uvicorn", "--port", "80", "--host", "0.0.0.0", "--reload", "api:app"]

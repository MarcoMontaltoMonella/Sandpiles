FROM python:3
ADD . /
WORKDIR /
ENV PYTHONPATH /
RUN pip install -r requirements.txt
CMD [ "python", "./src/__main__.py" ]

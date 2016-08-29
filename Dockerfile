FROM python:2.7
# COPY pip.conf /root/.pip/pip.conf
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt

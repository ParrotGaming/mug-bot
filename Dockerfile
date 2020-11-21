FROM ubuntu:18.04

WORKDIR /usr/src/app
RUN apt-get update && apt-get install -y \
        software-properties-common
    RUN add-apt-repository ppa:deadsnakes/ppa
    RUN apt-get update && apt-get install -y \
        python3.7 \
        python3-pip
    RUN python3.7 -m pip install pip
    RUN apt-get update && apt-get install -y \
        python3-distutils \
        python3-setuptools

COPY /project .

RUN pip3 install -r requirements.txt

CMD python3 bot.py
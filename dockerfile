FROM ubuntu:22.04
RUN apt update

RUN apt install python3-pip -y
COPY requirements.txt ./
RUN pip3 install

WORKDIR /app

COPY . .

CMD ["python3","-m","flask","run","--host:5000"]


FROM ubuntu:22.04

RUN apt update && apt install -y python3-pip

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

WORKDIR /app

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

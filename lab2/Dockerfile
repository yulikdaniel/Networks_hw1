FROM python:3.8-slim

RUN apt-get update -y && apt-get install -y iputils-ping

COPY host_mtu.py .

ENTRYPOINT ["python3", "host_mtu.py"]
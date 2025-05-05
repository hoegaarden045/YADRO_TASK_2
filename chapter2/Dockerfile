FROM ubuntu:22.04

WORKDIR app

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install requests && \
    rm -rf /var/cache/apt

COPY script.py .
RUN chmod +x script.py
CMD ["python3", "script.py"] 

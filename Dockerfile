# Dockerfile
FROM python:3.12.3-slim
RUN apt-get update && \
    apt-get install -y pkg-config libhdf5-hl-100 libhdf5-dev gcc
WORKDIR /root
COPY requirements.txt /root/
RUN pip install -r requirements.txt
COPY app /root/app
# Run fetch of model
#ENTRYPOINT ["uwsgi"]
#CMD ["uwsgi config/wsgi_main.ini"]
ENTRYPOINT ["python"]
CMD ["app/main.py"]
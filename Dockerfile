# Dockerfile
FROM python:3.12.3-slim
WORKDIR /root
COPY requirements.txt /root/
RUN pip install -r requirements.txt
COPY app /root/app
# Run fetch of model
#ENTRYPOINT ["uwsgi"]
#CMD ["uwsgi config/wsgi_main.ini"]
ENTRYPOINT ["python"]
CMD ["app/main.py"]
# Dockerfile
FROM python:3.12.3-slim
# Dependencies: pkg-config/libhdf5-*/gcc for tensorflow, wget for collecting phishing_model.keras
RUN apt-get update && \
    apt-get install -y pkg-config libhdf5-hl-100 libhdf5-dev gcc wget
WORKDIR /root
COPY requirements.txt /root/
RUN pip install -r requirements.txt
COPY app /root/app
# Run fetch of latest model
RUN mkdir /root/models
RUN wget https://github.com/remla24-team-1/model-training/raw/main/models/phishing_model.keras -P /root/models/

COPY config /root/config
EXPOSE 6788:6788
#ENTRYPOINT ["uwsgi"]
#CMD ["uwsgi config/wsgi_main.ini"]
#ENTRYPOINT ["bash"]
ENTRYPOINT ["python"]
CMD ["app/main.py"]
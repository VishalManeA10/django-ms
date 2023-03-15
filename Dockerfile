FROM python:3.10-slim-buster
COPY requirement.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 9001
COPY . .
CMD [ "python3", "manage.py","runserver","0.0.0.0:9001"]
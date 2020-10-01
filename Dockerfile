FROM python:3
ENV PYTHONUNBUFFERED=1

RUN mkdir /src
RUN mkdir /static

WORKDIR /src

COPY src/requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

CMD python manage.py collectstatic --no-input; python manage.py migrate; python manage.py runserver 0.0.0.0:8001


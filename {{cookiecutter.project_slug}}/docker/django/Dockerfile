FROM python:3.5

ENV PYTHONUNBUFFERED 1

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements /requirements

RUN pip install -r /requirements/production.txt \
    && groupadd -r django \
    && useradd -r -g django django

COPY ./docker/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY . /app
RUN chown -R django /app

COPY ./docker/django/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh \
    && chmod +x /start.sh \
    && chown django /start.sh

WORKDIR /app

RUN mkdir /data \
    && chown django.django /data

RUN mkdir /data/static \
    && chown django.django /data/static

RUN mkdir /data/media \
    && chown django.django /data/media

ENTRYPOINT ["/entrypoint.sh"]

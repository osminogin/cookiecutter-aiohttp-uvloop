FROM python:3.7-slim

ENV PATH /root/.local/bin:$PATH
ARG BUILD_DATE
ARG VCS_REF
ENV PYTHONUNBUFFERED 1
ENV PORT 8000

LABEL maintainer="osintsev@gmail.com" \
    org.label-schema.build-date="$BUILD_DATE" \
    org.label-schema.docker.cmd="docker run --rm --publish ${PORT}:8000 --name {{cookiecutter.project_slug}}" \
    org.label-schema.name="{{cookiecutter.description}}" \
    org.label-schema.vcs-ref="$VCS_REF" \
    org.label-schema.schema-version="1.0"

HEALTHCHECK --start-period=5 --retries=2 \
    CMD "/usr/bin/curl -f http://127.0.0.1/ping/"

COPY . /app
WORKDIR /app

RUN apt-get -y update && \
    apt-get -y install python3-dev make postgresql-client-common postgresql-client-11 redis-tools curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    pip3 install --no-warn-script-location --user pipenv && \
    pipenv install

EXPOSE $PORT

CMD ["make", "daemon"]

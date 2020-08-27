FROM python:3.7-slim

ENV PATH /root/.local/bin:$PATH
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION

ENV PYTHONUNBUFFERED 1
ENV PORT 8000
ENV GUNICORN_WORKERS=2
ENV GUNICORN_BACKLOG=4096

LABEL maintainer="{{cookiecutter.email}}" \
    org.label-schema.build-date="$BUILD_DATE" \
    org.label-schema.docker.cmd="docker run --rm {% if cookiecutter.use_postgres == 'y' %} --link postgres{% endif %}{% if cookiecutter.use_redis == 'y' %} --link redis{% endif %} --publish $PORT:8000 --name {{cookiecutter.project_slug}}" \
    org.label-schema.name="{{cookiecutter.description}}" \
    org.label-schema.license="MIT" \
    org.label-schema.usage="https://github.com/osminogin/cookiecutter-aiohttp-uvloop#usage" \
    org.label-schema.vcs-ref="$VCS_REF" \
    org.label-schema.schema-version="1.0" \
    org.label-schema.version="$VERSION"


HEALTHCHECK --start-period=5s --retries=2 CMD "/usr/bin/curl -f http://127.0.0.1/ping/"

COPY .. /app
WORKDIR /app

RUN apt-get -y update && \
    apt-get -y install python3-dev make{% if cookiecutter.use_postgres == 'y' %} postgresql-client-common postgresql-client-11{% endif %}{% if cookiecutter.use_postgres == 'y' %} redis-tools{% endif %} curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    pip3 install --no-warn-script-location --user pipenv && \
    pipenv install

EXPOSE $PORT

CMD ["make", "daemon"]

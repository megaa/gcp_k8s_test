###########
# BUILDER #
###########

# pull official base image
FROM python:3.9.15-alpine AS builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install psycopg2 and Pillow dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# lint
RUN pip install --upgrade pip
#RUN pip install flake8
#COPY . .
#RUN flake8 --ignore=E501,F401 .

# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM python:3.9.15-alpine

# create directory for the app user
RUN mkdir -p /home/dduser

# create the app user
ARG USER=dduser
ARG UID=1901
ARG GID=1901
RUN adduser -u ${UID} -D ${USER}

# create the appropriate directories
ENV HOME=/home/dduser
ENV APP_HOME=/home/dduser/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
RUN apk update
RUN apk add \
    libpq \
    openssl \
    bash \
    tzdata
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy entrypoint.sh
COPY ./entrypoint.sh $APP_HOME

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R ${USER}:${USER} $APP_HOME

# change to the app user
USER ${UID}:${GID}

# run entrypoint.prod.sh
ENTRYPOINT ["/home/dduser/web/entrypoint.sh"]

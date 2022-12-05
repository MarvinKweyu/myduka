# pull official base image
FROM python:3.9.6-alpine

# set working directory
WORKDIR /usr/src/myduka

# environment variables
ENV PYTHONDONTWRITEBYTECODE 1
# DON'T BUFFER STDOUT AND STDERR
ENV PYTHONUNBUFFERED 1

# psycopg deps
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/myduka/entrypoint.sh
RUN chmod +x /usr/src/myduka/entrypoint.sh
# copy project
COPY . .
RUN ls /usr/src/myduka

# run entrypoint
ENTRYPOINT [ "/usr/src/myduka/entrypoint.sh" ]

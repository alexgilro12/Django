FROM python:3.13.5-alpine3.22

WORKDIR /app

COPY ./requirements.txt ./

RUN apk update \
    && apk add --no-cache gcc musl-dev linux-headers libffi-dev \
    && pip install --upgrade pip 

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

CMD ["python", "manage.py", "runserver", "0.0.0:8000"]
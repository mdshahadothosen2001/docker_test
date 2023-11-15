FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./backend/requirements/development.txt /app/backend/requirements/
RUN pip install -r backend/requirements/development.txt

COPY . .
EXPOSE 8010

CMD ["python", "manage.py", "runserver", "0.0.0.0:8010"]

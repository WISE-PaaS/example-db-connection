FROM python:3.7-alpine

COPY . /app
WORKDIR /app
RUN pip install pipenv
RUN pipenv install --deploy --system --ignore-pipfile

EXPOSE 5000
CMD ["python", "main.py"]
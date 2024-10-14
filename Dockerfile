FROM python:3.12.0-slim

WORKDIR /app

RUN apt-get update && apt-get install -y make

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry

RUN poetry install --only main --no-interaction --no-ansi

COPY . /app

RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["make", "run"]
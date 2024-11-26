FROM python3.12.3

RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry install

COPY ./app .

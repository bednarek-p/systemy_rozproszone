FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_VERSION=1.2.1

RUN pip install --upgrade pip

WORKDIR /app/src

# Copy code to container
COPY poetry.lock pyproject.toml ./
COPY /src ./

# RUN poetry install
RUN pip install poetry

# Run app
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root
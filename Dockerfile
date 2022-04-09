FROM --platform=linux/amd64 python:3.9-slim

# Set pip to have cleaner logs and no saved cache
ENV PIP_NO_CACHE_DIR=false \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    POETRY_VIRTUALENVS_CREATE=false

# Install poetry
RUN python -m pip install -U pip \
    && pip install -U setuptools wheel \
    && apt-get update \
    && apt-get install -y curl python3-dev git \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
ENV PATH="${PATH}:/root/.poetry/bin"

# Copy the project files into working directory
WORKDIR /sagira
COPY pyproject.toml poetry.lock ./

# Install project dependencies
RUN poetry install --no-dev --no-interaction --no-ansi

# Copy the code after install so changes don't invalidate the earlier image layers
COPY . .

# TODO: add HEALTHCHECK

ENTRYPOINT ["python3"]
CMD ["-m", "sagira"]

# Define docker persistent volumes
VOLUME /sagira/log /sagira/data

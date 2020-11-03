FROM python:3.8-alpine3.12

# Set pip to have cleaner logs and no saved cache
ENV PIP_NO_CACHE_DIR=false \
    PIPENV_HIDE_EMOJIS=1 \
    PIPENV_IGNORE_VIRTUALENVS=1 \
    PIPENV_NOSPIN=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Copy the project files into working directory
WORKDIR /bot
COPY . .

# Install pipenv and project dependencies
# '--virtual': https://stackoverflow.com/a/49714913
RUN apk add --no-cache --virtual .build-deps alpine-sdk \
  && pip install pipenv \
  && pipenv install --deploy --system \
  && apk del .build-deps

ENTRYPOINT ["python"]
CMD ["-m", "bot"]

# Define docker persistent volumes
VOLUME /bot/bot/log /bot/data

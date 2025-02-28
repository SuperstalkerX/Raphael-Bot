# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-buster


ENV BOT_PREFIX=","
ENV BOT_TOKEN=""
ENV BOT_ID=""
ENV LOG_LEVEL="INFO"
ENV SENTRY_DSN=""
ENV FINNHUB_TOKEN=""

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "raphael.py"]

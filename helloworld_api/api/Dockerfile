FROM python:3.9-alpine
WORKDIR /src
COPY ./requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt
COPY ./app /src/app

# APP CONFIG ----------------------------------------------------------------

ENV APP_NAME="Context Lab - FastAPI - Hello World"
ENV APP_VERSION="0.0.2"
ENV DEBUG_FLAG="0"

# SPECIFY DEPLOYMENT TYPE ---------------------------------------------------
#ENV APP_DEPLOYMENT="production"
ENV APP_DEPLOYMENT="dev"

ENV UID_LENGTH="7"

ENV LOCAL_URL="0.0.0.0:3001"
ENV PROD_URL="unknown.com"

# AUTH CONFIG ----------------------------------------------------------------
ENV API_KEY_HEADER="api-key"

# MONGODB ----------------------------------------------------------------
ENV LOG_IP_HEADERS="true"
ENV LOG_TO_DB="true"

# COMMANDS ----------------------------------------------------------------
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]

FROM python:3.9

RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common build-essential gcc git curl cmake \
    vim zip sudo nano openssh-server wget ca-certificates netbase procps libpq-dev nginx supervisor

WORKDIR /app

RUN mkdir /app/api
RUN mkdir /app/frontend


COPY api/ /app/api/
COPY frontend/ /app/frontend/
COPY gunicorn/ /app/gunicorn/
COPY supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

WORKDIR /app/api

RUN pip install -r requirements.txt

EXPOSE 8000

# CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]
# CMD ["/bin/bash"]

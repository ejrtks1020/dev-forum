FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common build-essential gcc git curl cmake \
    vim zip sudo nano openssh-server wget ca-certificates netbase procps libpq-dev nginx supervisor

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

# CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]
# CMD ["/bin/bash"]

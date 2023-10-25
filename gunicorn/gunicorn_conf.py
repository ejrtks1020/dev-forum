name = 'api-service-python-script'
# bind = 'unix:/tmp/gunicorn.sock'
bind = '0.0.0.0:8000'

workers = 2
# workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'uvicorn.workers.UvicornWorker'
#worker_class = "gevent"
worker_connections = 1000 * workers
keepalive = 32
reload = True

capture_output = True
log_level = 'info'
errorlog = '-'
accesslog = '-'
spew = False

max_requests = 1000
max_requests_jitter = 50
graceful_timeout = 15
timeout = 0                 # No Timeout

BASE_DIR = "/app/api"
chdir = BASE_DIR


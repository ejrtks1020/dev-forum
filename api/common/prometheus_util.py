from prometheus_client import generate_latest, REGISTRY, Counter, Gauge, Histogram

REQUESTS = Counter(name='http_requests_total', documentation='Total HTTP Requests (count)', labelnames=['method', 'endpoint', 'status_code'])
IN_PROGRESS = Gauge(name='http_request_inprogress', documentation='Number of in progress HTTP requests')
TIMINGS = Histogram(name='http_request_duration_seconds', documentation='HTTP request latency (seconds)')

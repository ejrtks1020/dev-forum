from fastapi import FastAPI, Response
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
from router import question_router, answer_router, user_router
import os
from common.prometheus_util import *

app = FastAPI()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

folder = os.path.dirname(__file__)

app.include_router(question_router.router)
app.include_router(answer_router.router)
app.include_router(user_router.router)
app.mount("/assets", StaticFiles(directory="../frontend/dist/assets"))

@IN_PROGRESS.track_inprogress()
@TIMINGS.time()
@app.get('/metrics')
def metrics():
    REQUESTS.labels(method='GET', endpoint="/metrics", status_code=200).inc()
    return Response(
            media_type="text/plain",
            content=generate_latest()
            )

@app.get("/")
def index():
    return FileResponse("../frontend/dist/index.html")

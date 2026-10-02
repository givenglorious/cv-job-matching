from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.database import init_db
from app.routes import criteria, upload, results

app = FastAPI(title="CV Autochecker")

app.include_router(criteria.router)
app.include_router(upload.router)
app.include_router(results.router)


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/")
def home():
    return RedirectResponse(url="/criteria")

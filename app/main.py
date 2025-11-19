from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from api import routes
app = FastAPI(title="RAGForge Dashboard")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(routes.router)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "RAGForge Dashboard"})

@app.get("/query", response_class=HTMLResponse)
async def query_page(request: Request):
    return templates.TemplateResponse(
        "query.html",
        {"request": request, "title": "Query Engine"}
    )

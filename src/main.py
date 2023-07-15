import uvicorn

from classes import DividerText, Searcher, AnalyzerText

from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from pathlib import Path


app = FastAPI()

templates_dir = Path(__file__).resolve().parent / "templates"
templates = Jinja2Templates(directory=str(templates_dir))


@app.get("/", response_class=HTMLResponse)
def get_front(request: Request):
    return templates.TemplateResponse("front.html", {"request": request})


@app.post("/unique_symbol", response_class=HTMLResponse)
def receive_text(request: Request, sentence: str = Form(...)):
    divider_text = DividerText()
    searcher_unique = Searcher()
    analyzer_text = AnalyzerText(sentence, divider_text, searcher_unique)
    most_unique_symbol = analyzer_text.get_most_unique_symbol()
    return templates.TemplateResponse("result.html", {"request": request, "symbol": most_unique_symbol})


if __name__ == "__main__":
    config = uvicorn.Config("main:app", host="0.0.0.0", port=8000, reload=True)
    server = uvicorn.Server(config)
    server.run()

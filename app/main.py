from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.model import generate_text, search_cocktail
from app.schema import UserInput

app = FastAPI()

templates = Jinja2Templates(directory="app/static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat(user_input: UserInput):
    response= search_cocktail(user_input.message)
    if response:
        return {"response": generate_text(response[0]["name"], response[0]["description"])}
    else:
        return {"response": "Sorry, I couldn't find any cocktails with that name."}


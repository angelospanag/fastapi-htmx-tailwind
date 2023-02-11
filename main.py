import pathlib
import random
import string

import pandas as pd
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

BASE_DIR = pathlib.Path.cwd()
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/tab1", response_class=HTMLResponse)
async def tab1(request: Request):
    return templates.TemplateResponse("tab1.html", {"request": request})


def random_string(length):
    letters = string.ascii_letters
    return "".join(random.choice(letters) for i in range(length))


@app.get("/tab2", response_class=HTMLResponse)
async def tab2(request: Request):
    people = [
        {
            "Name": random_string(10),
            "Age": random.randint(20, 70),
            "City": random_string(15),
        }
        for _ in range(1000)
    ]
    df = pd.DataFrame(people)
    return templates.TemplateResponse(
        "tab2.html", {"request": request, "data": df.to_dict("records")}
    )


@app.get("/tab3", response_class=HTMLResponse)
async def tab3(request: Request):
    return templates.TemplateResponse("tab3.html", {"request": request})

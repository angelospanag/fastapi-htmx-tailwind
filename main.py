import pathlib
import random
from collections import OrderedDict

import polars as pl
from faker import Faker
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# FastAPI
app = FastAPI()

# Faker
locales = OrderedDict(
    [
        ("en", 1),
    ]
)
fake = Faker(locales)

# Static assets path
BASE_DIR = pathlib.Path.cwd()
app.mount("/static", StaticFiles(directory=BASE_DIR / "ui" / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "ui" / "templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/tab1", response_class=HTMLResponse)
async def tab1(request: Request):
    return templates.TemplateResponse("tab1.html", {"request": request})


@app.get("/tab2", response_class=HTMLResponse)
async def tab2(request: Request):
    people = [
        {
            "Name": fake.name(),
            "Age": random.randint(20, 70),
            "Address": fake.address(),
        }
        for _ in range(50)
    ]

    df = pl.DataFrame(people)
    return templates.TemplateResponse(
        "tab2.html", {"request": request, "columns": df.columns, "data": df.to_dicts()}
    )


@app.get("/tab3", response_class=HTMLResponse)
async def tab3(request: Request):
    return templates.TemplateResponse("tab3.html", {"request": request})

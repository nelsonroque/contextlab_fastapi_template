from datetime import date, datetime
import time
from json import JSONDecoder
import re
from urllib import response
from typing import Union
from jinja2 import Template
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# INIT APP

# - start new FastAPI
# - TODO: add more metadata: https://fastapi.tiangolo.com/tutorial/metadata/

app = FastAPI(title="Context Lab - FastAPI - Hello World",
            debug=True,
            version="0.0.01",
            contact={
                    "name": "Nelson Roque, PhD",
                    "url": "https://nelsonroque.com",
                    "email": "nelson.roque@ucf.edu",
                }
)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# MOUNT FILES

# - mount common files/libaries
# app.mount("/common", StaticFiles(directory="app/common"), name="common_assets")

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# REQUEST LIFECYLE

@app.on_event("startup")
async def startup_event():
    et = datetime.now()
    start_iso = et.isoformat()
    print(f"[{start_iso}]: startup")

@app.on_event("shutdown")
async def shutdown_event():
    et = datetime.now()
    start_iso = et.isoformat()
    print(f"[{start_iso}]: shutdown")

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# MIDDLEWARE

# - add custom middleware for logging
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):

    # get time info
    start_time = time.time()
    start_iso = datetime.now()
    response2 = await call_next(request)
    end_time = time.time()

    # calculate process time
    process_time = end_time - start_time

    # append headers
    response2.headers["X-Process-StartTime_ISO"] = str(start_iso.isoformat())
    response2.headers["X-Process-TotalTime"] = str(process_time)
    
    return response2

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Middleware
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# prepare homepage for `Palabras`
@app.get("/", tags=["homepage"])
async def render_homepage():
  html = "<h1>Hello World</h1>"
  template = Template(html)
  html_template_string = template.render()
  return HTMLResponse(html_template_string, status_code=200, headers={"Content-Type": "text/html", "Access-Control-Allow-Origin": "*"})
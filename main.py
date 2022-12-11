from fastapi import FastAPI, Header, Request
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/about")
def hello():
    return HTMLResponse("<h3>Hello, ainur new-about-response 2</h3>")

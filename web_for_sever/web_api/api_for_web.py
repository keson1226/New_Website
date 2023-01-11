from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from typing import Optional
from pydantic import BaseModel
from web_for_sever.web_scraping.key_words_scraping import hot_key_dict

def html_create():
    html_contents ="""
<head>
    <title>LifeTool</title>
</head>
<body>
    <div class="above_selection">
        <a id="web_Home" href="guest.html">LifeTool</a>
        <a href="date.html">Date</a>
        <a>Weather</a>
        <a>Note</a>
        <a>Flavorite Web</a>
        <a>Keys</a>
        <a>Login</a>
    </div>
    <div>
        <p>Home</p>
    </div>
</body>
    """
    return HTMLResponse(content=html_contents,status_code=200)

title = "My API"

app=FastAPI(title=title)

@app.get(
    "/",
    tags=["Guest"]
)
def welcome(page : Optional[str] = None):
    if page:
        return f"There is Page {page} !"
    else:
        return "There is no Page !"


@app.get(
    "/ok",
    tags=["Guest"]
)
def sayhello():
    return "Hello"

class Charact(BaseModel):
    name : str
    age : Optional[int]
    isMale : bool

@app.post(
    "/charact",
    tags=["Player"]
)
def create_charact(player : Charact):
    return f"Your Charact is created with name as {player.name}"


@app.get(
    "/guest.html"
)
def see_web():
    return html_create()

@app.post(
    "/hot_key",
    tags=["web"]
)
def search_key( area : Optional[str] = None ):
    if area :
        return hot_key_dict(area)
    return hot_key_dict()
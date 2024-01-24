# Import API Setting Module
from typing import Optional
from fastapi import FastAPI,Query,Response
from fastapi.middleware.cors import CORSMiddleware

# Import Response Model
from web_backend.schema.hot_key_response_schema import HotKeyResponseModel

# Import Request Model
pass

# Import Scripts
from web_backend.scripts.hot_key_scraping import Scraping_hot_key



# Create API , Name is app.
title = "My API"
app=FastAPI(title=title)


# Create CORS Policy
origins = [
    "*"
] ## Allow Origins
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = False,
    allow_methods = ['GET'],
    allow_headers = ['*']
) ## Allow Access Setting


# API {GET "/"} START
@app.get(
    "/",
    tags=["Index"]
)
def get_homePage():
    return {}
# API {GET "/"} END


# API {GET "hot_key"} START
geo_list=[]
@app.get(
    "/hot_key",
    tags=["Hot Key"],
    response_model=HotKeyResponseModel,
)
async def search_key( 
    geo : Optional[str] = Query("TW" , description="The country's name that you are searching for(using two charact)."),
    endDate : Optional[str] = Query("" , description="The end you want search !"),
    response : Response = None
): 
    if endDate != "":
        endDate = f"&ed={endDate}"
    if geo == None:
        geo = "tw"
    
    scraping_result = await Scraping_hot_key(geo=geo,endDate=endDate)
    if scraping_result[0] : print('Success')
    return scraping_result[1] 
# API {GET "hot_key"} END


# API {} START
@app.get(
    "/time",
    tags=["Date & Time"],
    response_model=None
)
def get_time():
    return {}
# API {} END



# API Testing Field
## GET
@app.get(
    "/test/get",
    tags=["Testing"],
    response_model=None
)
def test_get():
    """GET Testing"""
    return {
        "status" : "ok",
        "code" : 200
    }

## POST
@app.post(
    "/test/post",
    tags=["Testing"],
    response_model=None
)
def test_post():
    """POST Testing"""
    return {
        "status" : "ok",
        "code" : 200
    }

## PUT
@app.put(
    "/test/put",
    tags=["Testing"],
    response_model=None
)
def test_put():
    """PUT Testing"""
    return {
        "status" : "ok",
        "code" : 200
    }

## PATCH
@app.patch(
    "/test/patch",
    tags=["Testing"],
    response_model=None
)
def test_patch():
    """PATCH Testing"""
    return {
        "status" : "ok",
        "code" : 200
    }

## DELETE
@app.delete(
    "/test/delete",
    tags=["Testing"],
    response_model=None
)
def test_delete():
    """DELETE Testing"""
    return {
        "status" : "ok",
        "code" : 200
    }

## HEAD
@app.head(
    "/test/head",
    tags=["Testing"],
    status_code=204
)
def test_head():
    """HEAD Testing"""
    # response.status_code = 204

## OPTIONS
@app.options(
    "/test/options",
    tags=["Testing"],
    response_model=None
)
def test_options():
    """OPTIONS Testing"""
    return {
        "status" : "ok",
        "code" : 200
    }

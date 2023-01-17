from typing import Optional

from fastapi import FastAPI,Query
from pydantic import BaseModel

from web_for_sever.web_api.scraping_schema import DayResponseListModel
from web_for_sever.web_scraping.key_words_scraping import hot_key_dict

#create API , name is app.
title = "My API"
app=FastAPI(title=title)

# API "/" using GET() return {}
@app.get(
    "/",
    tags=["Root"]
)
def get_homePage():
    return {}

geo_list=[
    
]
@app.get(
    "/hot_key",
    tags=["Hot Key"],
    response_model=DayResponseListModel
)
async def search_key( 
    geo : Optional[str] = Query(None , description="The country's name that you are searching for(using two charact)."),
    endDate : Optional[str] = Query("" , description="The end you want search !")
): 
    if endDate != "":
        endDate = f"&ed={endDate}"
    if geo ==None:
        geo = "tw"
    
    return await hot_key_dict(country=geo,endDate=endDate)

@app.get(
    "/time",
    tags=["Date & Time"],
    response_model=None
)
def get_time():
    pass
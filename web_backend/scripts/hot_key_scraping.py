#### Import------------------------------
# Import Request Module
from json import loads as jsonLoads
from requests import get as getRequest

# Import Response Model
from web_backend.schema.hot_key_response_schema import (KeyResponseModel, DayResponseModel, ImageResponseModel, HotKeyResponseModel)

# Import DB Module
from web_backend.db_control.db_main import insert_hot_key


#### Scraping Data from Resource URL------------------------------
async def __scraping_raw_data(resource_url:str) -> dict:
    """Scraping "Hot Key" Raw Data"""
    response = getRequest(resource_url) ## sent GET request and catch response
    raw_data = response.text[5:] ## get data content & remove useless character

    response.close() ## release trash

    return dict(jsonLoads(raw_data)) ## turn response to JSON format


#### Classify Response Data------------------------------
def __data_classing(geo:str, data:dict) -> tuple[bool, HotKeyResponseModel]:
    default = data["default"]; del data  ## data.default

    if default["trendingSearchesDays"]:
        endDateForNextRequest = default["endDateForNextRequest"] ## data.default.endDateForNextRequest
        trendingSearchesDays = default["trendingSearchesDays"];  del default ## data.default.trendingSearchesDays

        for index, day in enumerate(trendingSearchesDays):
            date = int(day["date"]) ## data.default.trendingSearchesDays[index].date
            formattedDate = day["formattedDate"] ## data.default.trendingSearchesDays[index].formattedDate
            trendingSearches = day["trendingSearches"] ## data.default.trendingSearchesDays[index].trendingSearches

            for tag, search in enumerate(trendingSearches):
                title = search["title"]["query"] ## data.default.trendingSearchesDays[index].trendingSearches[tag].title.query
                formattedTraffic = search["formattedTraffic"] ## data.default.trendingSearchesDays[index].trendingSearches[tag].formattedTraffic
                image = search["image"] ## data.default.trendingSearchesDays[index].trendingSearches[tag].image
                try:
                    imageUrl = image["imageUrl"] ## data.default.trendingSearchesDays[index].trendingSearches[tag].image.imageUrl
                except:
                    trendingSearches[tag] = KeyResponseModel(key_title=title, key_hot=formattedTraffic)
                else:
                    source = image["source"] ## data.default.trendingSearchesDays[index].trendingSearches[tag].image.source
                    newsUrl = image["newsUrl"] ## data.default.trendingSearchesDays[index].trendingSearches[tag].image.newsUrl
                    image = ImageResponseModel(image_link=imageUrl, source=source, news_link=newsUrl)
                    trendingSearches[tag] = KeyResponseModel(key_title=title, key_hot=formattedTraffic, image=image)
            
            trendingSearchesDays[index] = DayResponseModel(day_date_int=date, day_date_string=formattedDate, key_list=trendingSearches)
        
        return (True, HotKeyResponseModel(geo=geo, endDateForNextRequest=endDateForNextRequest, day_list=trendingSearchesDays))
    
    else : 
        return (False, HotKeyResponseModel(geo=geo))



#### 尋找關鍵字------------------------------
async def Scraping_hot_key(geo:str ="TW" , endDate:str = "") -> HotKeyResponseModel :
    
    geo = geo.upper() ## normalize query format
    apiUrl = f"https://trends.google.com.tw/trends/api/dailytrends?hl=zh-TW&tz=-480{endDate}&geo={geo}&ns=15" ## set api url

    raw_data = await __scraping_raw_data(apiUrl) ## scraping "hot key" raw data
    classed_data = __data_classing(geo, raw_data) ## classing raw data

    try:
        if not classed_data[0] : raise Exception("End Date Query Error")
    except Exception as e:
        print(e)
    else:
        await insert_hot_key(classed_data[1])

    return classed_data ## return scraping result
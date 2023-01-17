import json

import requests

from web_for_sever.web_api.scraping_schema import (KeyResponseModel, DayResponseModel, ImageResponseModel, DayResponseListModel)

async def get_from_link(link):
    info = requests.get(link)
    data = info.text
    info.close()
    return data

async def hot_key_dict(country : str ="TW" , endDate : str = "") -> dict :
    
    country = country.upper()
    url = "https://trends.google.com.tw/trends/api/dailytrends?hl=zh-TW&tz=-480{}&geo={}&ns=15"
    url = url.format(endDate,country)

    datas_text = await get_from_link(url)
    datas_text = datas_text[5:]
    datas_json = json.loads(datas_text)
    del datas_text

    hot_key_info = DayResponseListModel()
    hot_key_info.endDateForNextRequest = datas_json["default"]["endDateForNextRequest"]
    days_key_info = []
    
    days_datas = datas_json["default"]["trendingSearchesDays"];del datas_json
    for day_datas in days_datas:
        
        keys_of_day = DayResponseModel()
        keys_of_day.day_date_int = int(day_datas["date"])
        keys_of_day.day_date_string = day_datas["formattedDate"]

        keys_datas = day_datas["trendingSearches"]

        keys_list = []

        keys_amoung = len(keys_datas)
        for i in range(keys_amoung):

            key_data = keys_datas[i]

            key = KeyResponseModel()
            key.key_title = key_data["title"]["query"]
            key.key_hot = key_data["formattedTraffic"]

            image = ImageResponseModel()
            try:
                image.image_link = key_data["image"]["imageUrl"]
            except:
                del image
            else:
                image.source = key_data["image"]["source"]
                image.news_link = key_data["image"]["newsUrl"]
                key.image = image

            keys_list.append(key)
        keys_of_day.key_list = keys_list
        
        days_key_info.append(keys_of_day)
    
    hot_key_info.day_list=days_key_info

    return hot_key_info

# web=hot_key_dict("GB")
# with open("data.json","w") as file:
#     file.write(json.dumps(web))

import requests
import json


def hot_key_dict(country : str ="TW") -> dict :
    country = country.upper()
    url = "https://trends.google.com.tw/trends/api/dailytrends?hl=zh-TW&tz=-480&geo={}&ns=15"
    url = url.format(country)

    data =None

    with requests.get(url) as req:
        data = req.text

    data = data[5:]
    data = json.loads(data)

    data = data["default"]["trendingSearchesDays"][0]
    data_date = data["date"]
    data_date_string = data["formattedDate"]

    data = data["trendingSearches"]

    data_amoung = len(data)
    if data_amoung>10:
        data_amoung=10

    data_list = []

    for i in range(data_amoung):
        unit_data_dict = {}

        one_data = data[i]

        unit_data_dict["formattedTraffic"] = one_data["formattedTraffic"]
        unit_data_dict["title"] = one_data["title"]["query"]

        unit_data_img = {}

        unit_data_img["imageUrl"] = one_data["image"]["imageUrl"]
        unit_data_img["newsUrl"] = one_data["image"]["newsUrl"]
        unit_data_img["source"] = one_data["image"]["source"]

        unit_data_dict["image"] = unit_data_img

        data_list.append(unit_data_dict)

    response_dict = {
        "data_date" : data_date,
        "data_date_string" : data_date_string,
        "day_hot_key" : data_list
    }

    return response_dict

# web=hot_key_dict("GB")
# with open("data.json","w") as file:
#     file.write(json.dumps(web))

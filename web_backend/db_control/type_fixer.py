"""
    這個Module是用來: 將要儲存進資料庫的資料，做資料的前處理，避免TypeError
"""
# Import Data Schema
from web_backend.schema.hot_key_response_schema import (HotKeyResponseModel,DayResponseModel,KeyResponseModel,ImageResponseModel)


# Hot Key Data Dealing Functions
def __key_list_type_fixer(data:list[KeyResponseModel])->dict:
    for index, key in enumerate(data):
        data[index] = dict(key)
        try:
            data[index]['image'] = dict(data[index]['image']) # If image = None will throw ERROR
        except:
            pass
    return data
def __day_list_type_fixer(data:list[DayResponseModel])->dict:
    for index, day in enumerate(data):
        data[index] = dict(day)
        data[index]['key_list'] = __key_list_type_fixer(data[index]['key_list'] )
    return data
def hot_key_type_fixer(data:HotKeyResponseModel)->dict:
    """Change HotKeyResponseModel Type into Dict Type"""
    data = dict(data)
    data['day_list'] = __day_list_type_fixer(data['day_list'])
    return data
# Import Base Module
from pydantic import BaseModel,Field
from typing import Union

class ImageResponseModel(BaseModel):
    """Image Response Fields"""
    source : str=Field(
        title="Image Source",
        description="圖片出處",
        default=None
    )
    image_link : str=Field(
        title="Image Link",
        description="圖片連結",
        default=None
    )
    news_link : str=Field(
        title="News Link",
        description="包含此圖片的新聞連結",
        default=None
    )
    
class KeyResponseModel(BaseModel):
    """Key Response Fields"""
    key_title : str=Field(
        title="Key Title",
        description="關鍵字",
        default=None
    )
    key_hot : str = Field(
        title="Key Search Times",
        description="此關鍵字被搜尋的次數",
        default=None
    )
    image : Union[ImageResponseModel, None]=Field(
        title="Image Response Model",
        description="與這個關鍵字有關連的圖片",
        default=None
    )

class DayResponseModel(BaseModel):
    """Day Response Fields"""
    day_date_int : int = Field(
        title="Day Date Number",
        description="純數字的日期，用來表示此 Response 是哪一天的 Hot Key ，格式為：yyyymmdd，例如：20240101",
        default=None
    )
    day_date_string : str = Field(
        title="Day Date Word",
        description="""字串形式的日期，用來表示此 Response 是哪一天的 Hot Key ，格視為："xxxx年xx月xx日 星期x"，例如：2024年1月1日 星期一""",
        default=None
    )
    key_list : list[KeyResponseModel] = Field(
        title="Key List",
        description="這個 List 中存有當日的 Key Responses",
        default=None
    )


class HotKeyResponseModel(BaseModel):
    """Hot Key Response Fields"""
    geo : str = Field(
        title="Geo of Hot Keys",
        description="關鍵字發生熱搜的所在國家，由兩個大寫英文字母組合而成的字串，例如：'TW'代表的是臺灣"
    )
    endDateForNextRequest : str = Field(
        title="End Date Value For Next Request",
        description="進一步請求更多資料時，請將這個值帶入Query:endDate",
        default=None
    )
    day_list : list[DayResponseModel] = Field(
        title="A List Of Day Responses",
        description="這個 List 中存有不同日期的 Day Response",
        default=None
    )
    
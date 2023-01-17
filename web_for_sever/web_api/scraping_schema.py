from pydantic import BaseModel,Field
from typing import Optional

class ImageResponseModel(BaseModel):
    """Image Response Fields"""
    source : str=Field(
        title="Image Source",
        default=None
    )
    image_link : str=Field(
        title="Image Link",
        default=None
    )
    news_link : str=Field(
        title="News Link",
        default=None
    )
    
class KeyResponseModel(BaseModel):
    """Key Response Fields"""
    key_title : str=Field(
        title="Key Title",
        default=None
    )
    key_hot : str = Field(
        title="Key Search Times",
        default=None
    )
    image : Optional[ImageResponseModel]=Field(
        title="Image Response Model",
        default=None
    )

class DayResponseModel(BaseModel):
    """Day Response Fields"""
    day_date_int : int = Field(
        title="Day Date Number",
        default=None
    )
    day_date_string : str = Field(
        title="Day Date Word",
        default=None
    )
    key_list : list[KeyResponseModel] = Field(
        title="Key List",
        default=None
    )


class DayResponseListModel(BaseModel):
    """Day Response List"""
    endDateForNextRequest : str = Field(
        title="End Date For Next Request",
        default=None
    )
    day_list : list[DayResponseModel] = Field(
        title="Day List",
        default=None
    )
    
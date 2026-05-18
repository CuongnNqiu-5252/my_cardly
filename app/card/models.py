from typing import Optional

from pydantic import Field, BaseModel, HttpUrl, ConfigDict

from app.models import CustomModel

class ContactLinks(BaseModel):
    phone:     Optional[str]     = None
    email:     Optional[str]     = None
    zalo:      Optional[HttpUrl] = None
    whatsapp:  Optional[HttpUrl] = None
    linkedin:  Optional[HttpUrl] = None
    facebook:  Optional[HttpUrl] = None
    website:   Optional[HttpUrl] = None
    instagram: Optional[HttpUrl] = None
    tiktok:    Optional[HttpUrl] = None
    youtube:   Optional[HttpUrl] = None
    github:    Optional[HttpUrl] = None
    telegram:  Optional[HttpUrl] = None
    calendly:  Optional[HttpUrl] = None

    model_config = ConfigDict(extra="ignore")

class Card(CustomModel):
    user_id: Optional[str] = Field(..., alias="user_id")
    name: str = Field(...,alias="name")
    title: str = Field(default=None,alias="title")
    contact_links: Optional[ContactLinks] = Field(default=None,alias="contact_links")
    bio: Optional[str] = Field(default=None,alias="bio")
    highlight: Optional[list[str]] = Field(default=None,alias="highlight")
    profile_photo_url: Optional[HttpUrl] = Field(default=None,alias="profile_photo_url")
    custom_url : Optional[HttpUrl] = Field(default=None,alias="custom_url")
    is_published: Optional[bool] = Field(default=False, alias="is_published")
# class CardBuilder:
#     def __init__(self):
#         self._data = {}
#
#     def user_id(self, user_id: str):
#         self._data["user_id"] = user_id
#         return self
#
#     def name(self, name: str):
#         self._data["name"] = name
#         return self
#
#     def title(self, title: str):
#         self._data["title"] = title
#         return self
#
#     def bio(self, bio: str):
#         self._data["bio"] = bio
#         return self
#
#     def add_highlight(self, highlight: list[str]):
#         self._data["highlight"] = highlight
#         return self
#
#     def profile_photo(self, url: HttpUrl):
#         self._data["profile_photo_url"] = url
#         return self
#
#     def custom_url(self, url: HttpUrl):
#         self._data["custom_url"] = url
#         return self
#
#     def publish(self,is_published: bool):
#         self._data["is_published"] = is_published
#         return self
#
#     def contact_links(self, contactlinks: ContactLinks):
#         self._data["contact_links"] = contactlinks
#         return self
#
#     def build(self):
#         return Card(**self._data)
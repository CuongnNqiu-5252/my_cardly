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
    user_id: Optional[str] = Field(default=None, alias="user_id")
    name: str = Field(alias="name")
    title: str = Field(alias="title")
    contact_links: Optional[ContactLinks] = Field(alias="contact_links")
    bio: Optional[str] = Field(..., alias="bio")
    highlight: Optional[list[str]] = Field(..., alias="highlight")
    profile_photo_url: Optional[HttpUrl] = Field(..., alias="profile_photo_url")
    custom_url : Optional[HttpUrl] = Field(alias="custom_url")
    is_published: Optional[bool] = Field(default=False, alias="is_published")

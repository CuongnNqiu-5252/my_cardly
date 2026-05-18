from typing import Optional

from pydantic import BaseModel, Field, HttpUrl

from app.card.models import ContactLinks


class CardCreateSchema(BaseModel):
    name: str = Field(alias="name")
    title: str = Field(alias="title")
    contact_links: Optional[ContactLinks] = Field(alias="contact_links")
    bio: Optional[str] = Field(alias="bio")
    highlight: Optional[list[str]] = Field(alias="highlight")
    profile_photo_url: Optional[HttpUrl] = Field(alias="profile_photo_url")
    custom_url: Optional[HttpUrl] = Field(alias="custom_url")
    is_published: Optional[bool] = Field(default=False, alias="is_published")


class CardUpdateSchema(BaseModel):
    name: str = Field(alias="name")
    title: str = Field(alias="title")
    contact_links: Optional[ContactLinks] = Field(alias="contact_links")
    bio: Optional[str] = Field(alias="bio")
    highlight: Optional[list[str]] = Field(alias="highlight")
    profile_photo_url: Optional[HttpUrl] = Field(alias="profile_photo_url")
    custom_url: Optional[HttpUrl] = Field(alias="custom_url")
    is_published: Optional[bool] = Field(default=False, alias="is_published")

class CardResponse(BaseModel):
    name: str = Field(alias="name")
    title: str = Field(alias="title")
    contact_links: Optional[ContactLinks] = Field(alias="contact_links")
    bio: Optional[str] = Field(alias="bio")
    highlight: Optional[list[str]] = Field(alias="highlight")
    profile_photo_url: Optional[HttpUrl] = Field(alias="profile_photo_url")
    custom_url: Optional[HttpUrl] = Field(alias="custom_url")
    is_published: Optional[bool] = Field(default=False, alias="is_published")
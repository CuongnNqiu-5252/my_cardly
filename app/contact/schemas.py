from pydantic import BaseModel, Field
from pydantic.v1 import EmailStr

from app.card.models import ContactLinks


class CreateContact(BaseModel):
    name: str = Field(...,alias="name")
    email: EmailStr = Field(...,alias="email")
    phone: str = Field(...,alias="phone")
    event_id: str = Field(default=None,alias="event_id")
    user_id: str = Field(...,alias="user_id")
    contactLinks: ContactLinks
    address: str = Field(default=None,alias="address")
    website: str = Field(default=None,alias="website")
    company: str = Field(default=None,alias="company")
    country: str = Field(default=None,alias="country")

class UpdateContact(BaseModel):
    name: str = Field(...,alias="name")
    email: EmailStr = Field(...,alias="email")
    phone: str = Field(...,alias="phone")
    contactLinks: ContactLinks
    address: str = Field(default=None,alias="address")
    website: str = Field(default=None,alias="website")
    company: str = Field(default=None,alias="company")
    country: str = Field(default=None,alias="country")

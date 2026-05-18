from pydantic import Field
from pydantic.v1 import EmailStr

from app.card.models import ContactLinks
from app.models import CustomModel


class Contacts(CustomModel):
    email: EmailStr = Field(..., alias="email")
    phone_number: str = Field(...,alias="phone_number")
    full_name: str = Field(...,alias="full_name")
    user_id: str = Field(...,alias="user_id")
    event_id: str = Field(default=None,alias="event_id")
    address: str = Field(default=None,alias="address")
    company: str = Field(default=None,alias="company")
    country: str = Field(default=None,alias="country")
    website: str = Field(default=None,alias="website")
    contactLinks: ContactLinks = Field(default=None,alias="contactLinks")
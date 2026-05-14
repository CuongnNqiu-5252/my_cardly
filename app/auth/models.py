from pydantic import Field, EmailStr
from typing import Optional

from app.models import CustomModel


class User(CustomModel):


    username: str = Field(min_length=1, max_length=128, pattern="^[A-Za-z0-9-_]+$")
    email: EmailStr
    avatar_url: str
    password: str = Field(
        min_length=8,
        Optional=True,
    )

    my_card: list[str] = []
    def serializable_dict(self, **kwargs):
        return self.model_dump(
            by_alias=True,
            exclude={"id"},
            **kwargs
        )
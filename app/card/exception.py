from starlette import status

from app.exception import AppException


class CardNotFound(AppException):
    def __init__(self, message:str = "Card not found"):
        self.message = message
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            message=message,
            error_code="NOT_FOUND"
        )
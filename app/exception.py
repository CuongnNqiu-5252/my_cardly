from fastapi import HTTPException


class AppException(HTTPException):
    def __init__(
        self,
        status_code: int,
        message: str,
        error_code: str = "APP_ERROR"
    ):
        super().__init__(
            status_code=status_code,
            detail={
                "success": False,
                "error_code": error_code,
                "message": message
            }
        )
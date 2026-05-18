from fastapi import Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse



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


#========================Handler=====================

async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    errors = []
    for err in exc.errors():
        errors.append({
            "field": ".".join(map(str, err["loc"][1:])),
            "message": err["msg"],
            "type": err["type"]
        })

    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "error_code": "VALIDATION_ERROR",
            "message": "Request validation failed",
            "errors": errors
        }
    )


async def unhandled_exception_handler(
    request: Request,
    exc: Exception
):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error_code": "INTERNAL_SERVER_ERROR",
            "message": "Internal server error"
        }
    )
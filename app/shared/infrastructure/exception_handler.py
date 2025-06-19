from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.shared.domain import exceptions


def exception_handler(app: FastAPI) -> None:
    @app.exception_handler(exceptions.DatabaseConnectionException)
    def database_connection_exception_handler(
        _: Request,
        exc: exceptions.DatabaseConnectionException,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"success": False, "message": exc.message, "data": None},
        )

    @app.exception_handler(exceptions.IllegalArgumentException)
    def illegal_argument_exception_handler(
        _: Request,
        exc: exceptions.IllegalArgumentException,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"success": False, "message": exc.message, "data": None},
        )

    @app.exception_handler(exceptions.NotFoundException)
    def not_found_exception_handler(
        _: Request,
        exc: exceptions.NotFoundException,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"success": False, "message": exc.message, "data": None},
        )

    @app.exception_handler(exceptions.UninitializedException)
    def uninitialized_exception_handler(
        _: Request,
        exc: exceptions.UninitializedException,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"success": False, "message": exc.message, "data": None},
        )

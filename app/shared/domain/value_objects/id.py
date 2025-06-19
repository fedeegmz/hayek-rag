from typing import Annotated
from uuid import uuid4, UUID

from pydantic import BeforeValidator

from app.shared.domain.exceptions import IllegalArgumentException


def _ensure_is_valid(value: str | None = None) -> str:
    if value is None:
        return str(uuid4())
    try:
        return str(UUID(value))
    except ValueError:
        raise IllegalArgumentException(f"'{value}' is not a valid UUID.")


Id = Annotated[str, BeforeValidator(_ensure_is_valid)]

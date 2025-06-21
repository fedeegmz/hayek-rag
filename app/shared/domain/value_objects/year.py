from datetime import datetime
from typing import Annotated

from pydantic import BeforeValidator

from app.shared.domain.exceptions import IllegalArgumentException


def _ensure_is_valid(value: int) -> int:
    min_year = 1000
    current_year = datetime.now().year
    if isinstance(value, int) and min_year <= value <= current_year:
        return value
    raise IllegalArgumentException("Year must be between 1000 and current year.")


Year = Annotated[int, BeforeValidator(_ensure_is_valid)]

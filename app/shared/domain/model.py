from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field

from app.shared.domain.value_objects.id import Id


class Model(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Id = Field(default_factory=lambda: str(uuid4()))

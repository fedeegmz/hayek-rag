from typing import Annotated

from fastapi import Depends

from app.shared.infrastructure.adapters.voyage_embedding_generator import (
    VoyageEmbeddingGenerator,
)


def _get_voyage_embedding_generator() -> VoyageEmbeddingGenerator:
    return VoyageEmbeddingGenerator()


VoyageEmbeddingGeneratorDi = Annotated[
    VoyageEmbeddingGenerator, Depends(_get_voyage_embedding_generator)
]

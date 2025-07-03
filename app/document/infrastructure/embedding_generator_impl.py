from app.document.domain.embedding_generator import EmbeddingGenerator
from app.shared.domain.value_objects.embeddings import Embeddings
from app.shared.infrastructure.adapters.voyage_embedding_generator import (
    VoyageEmbeddingGenerator,
)


class EmbeddingGeneratorImpl(EmbeddingGenerator):
    def __init__(self, embedding_generator: VoyageEmbeddingGenerator) -> None:
        self.embedding_generator = embedding_generator

    async def generate(self, data: list[str]) -> Embeddings:
        return await self.embedding_generator.generate(data)

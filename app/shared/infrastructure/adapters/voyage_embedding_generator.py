import voyageai

from app.core.settings import settings
from app.shared.domain.embeddings import Embeddings


class VoyageEmbeddingGenerator:
    def __init__(self) -> None:
        self.model = "voyage-3-large"
        self.client = voyageai.AsyncClient(api_key=settings.embedding_api_key)

    async def generate(self, data: list[str]) -> Embeddings:
        result = await self.client.embed(texts=data, model=self.model)
        return result.embeddings

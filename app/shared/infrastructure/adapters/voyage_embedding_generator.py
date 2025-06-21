import voyageai

from app.core.settings import settings


class VoyageEmbeddingGenerator:
    def __init__(self):
        self.model = "voyage-3-large"
        self.client = voyageai.AsyncClient(api_key=settings.embedding_api_key)

    async def generate(self, data: list[str]) -> list[list[int | float]]:
        result = await self.client.embed(texts=data, model=self.model)
        return result.embeddings

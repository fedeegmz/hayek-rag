from google import genai

from app.chat.domain.llm import LLM
from app.core.settings import settings


class GeminiLLM(LLM):
    def __init__(self) -> None:
        self.model = "gemini-pro"
        self.client = genai.Client(api_key=settings.gemini_api_key)

    async def query(self, query: str | list[str]) -> str:
        response = await self.client.models.generate_content(
            model=self.model,
            contents=query,
        )
        return response.text

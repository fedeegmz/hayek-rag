from app.document.domain.author import Author
from app.shared.domain.embeddings import Embeddings
from app.shared.domain.model import Model
from app.shared.domain.value_objects.year import Year


class BaseDocument(Model):
    title: str
    author: Author = Author.HAYEK
    edition: Year
    collection: str | None = None


class Document(BaseDocument):
    embeddings: Embeddings = []

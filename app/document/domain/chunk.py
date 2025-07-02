from app.shared.domain.model import Model
from app.shared.domain.value_objects.embeddings import Embeddings
from app.shared.domain.value_objects.id import Id


class Chunk(Model):
    document_id: Id
    text: str
    embeddings: Embeddings = []

from sentence_transformers import SentenceTransformer
from typing import Any, List
import logging

logger = logging.getLogger(__name__)

class Embedding():
    model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

    def encode(self, source : Any) -> List[float]:
        try:
            res = self.model.encode(source).tolist() 
            logger.info("EMBEDDING: encode successfully")
        except Exception as e:
            logger.error(f"Error: {e}")
            res = []
        finally:
            return res  

embedding_client = Embedding()
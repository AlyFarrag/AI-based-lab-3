from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import Chroma
import numpy as np

class SentenceTransformerEmbeddings:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts):
        return self.model.encode(texts).tolist()

    def embed_query(self, query):
        return self.model.encode([query]).tolist()[0]

class EmbeddingEngine:
    def __init__(self):
        self.embedding_function = SentenceTransformerEmbeddings()
        self.vector_store = None

    def create_embeddings(self, texts):
        self.vector_store = Chroma.from_texts(texts, self.embedding_function)

    def search_similar(self, query, k=5):
        if self.vector_store:
            return self.vector_store.similarity_search(query, k=k)
        return []
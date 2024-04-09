import chromadb
import os
from utils.getRootPath import getRootPath
from sentence_transformers import SentenceTransformer
from models.index import getModelDefault
client = chromadb.PersistentClient(path=os.path.join(getRootPath(), 'data'))


def getResponses(query):
    collection = client.get_or_create_collection(
        name="collection",
        metadata={"hnsw:space": "cosine"}
    )
    model = SentenceTransformer(getModelDefault())
    queryEmbedding = model.encode([query.lower()])

    results = collection.query(
        query_embeddings=queryEmbedding,
        n_results=15,
        # where={"metadata_field": "is_equal_to_this"}, # optional filter
        # where_document={"$contains":"search_string"}  # optional filter
    )

    responses = [
    {
        "title": results["metadatas"][0][i]["title"],
        "content": results["metadatas"][0][i]["content"],
        "id": results["ids"][0][i],
        "document": results["documents"][0][i],
        "distance": results["distances"][0][i],
    }
    for i in range(len(results["ids"][0]))
]
    return responses
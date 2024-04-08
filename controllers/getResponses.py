import chromadb
import re
from sentence_transformers import SentenceTransformer
import chromadb.utils.embedding_functions as embedding_functions
from models.index import getModelDefault
client = chromadb.PersistentClient(path="../data")


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
        "id": results["ids"][0][i],
        "document": results["documents"][0][i],
        "distance": results["distances"][0][i],
    }
    for i in range(len(results["ids"][0]))
]
    print(responses)
    return responses
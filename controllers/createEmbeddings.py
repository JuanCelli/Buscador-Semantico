import chromadb
import re
import os
from sentence_transformers import SentenceTransformer
import chromadb.utils.embedding_functions as embedding_functions
client = chromadb.PersistentClient(path="../data")


from utils.openFileMd import openFileMd
from utils.spliteFile import splitFile
from utils.cleanText import cleanText
from utils.splitTitles import splitTitles
from models.index import getModelDefault
from utils.getRootPath import getRootPath




def createEmbeddings():
    collection = client.get_or_create_collection(
            name="collection",
            metadata={"hnsw:space": "cosine"}
    )

    fileRoute = os.path.join(getRootPath(), 'samples', 'archivo_v3.md')

    array = splitFile(openFileMd(fileRoute))
    arrayFiltered = [element for element in array if not (element.startswith("#") or element.startswith("##")) or element.startswith("###") or element.startswith("####")]


    arrayCleanText = [cleanText(chunk) for chunk in arrayFiltered]
    titles = [splitTitles(chunk) for chunk in arrayFiltered]



    print(len(arrayCleanText))
    arrayIds = [str(i) for i in range(len(arrayCleanText))]

    model = SentenceTransformer(getModelDefault())
    embeddings = model.encode(arrayCleanText)

    collection.add(
        documents=arrayCleanText,
        embeddings=embeddings,
        metadatas=titles,
        ids=arrayIds,
    )

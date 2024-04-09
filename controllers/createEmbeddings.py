import chromadb
import re
import os
from sentence_transformers import SentenceTransformer
import chromadb.utils.embedding_functions as embedding_functions


from utils.openFileMd import openFileMd
from utils.spliteFile import splitFile
from utils.getMetaDatas import getMetaDatas
from utils.splitTitles import splitTitles
from models.index import getModelDefault
from utils.getRootPath import getRootPath



client = chromadb.PersistentClient(path=os.path.join(getRootPath(), 'data'))

def createEmbeddings():
    collection = client.get_or_create_collection(
            name="collection",
            metadata={"hnsw:space": "cosine"}
    )

    fileRoute = os.path.join(getRootPath(), 'samples', 'archivo_v3.md')


    array = splitFile(openFileMd(fileRoute))[0]
    arrayOriginal = splitFile(openFileMd(fileRoute))[1]
    arrayFiltered = [element for element in array if not (element.startswith("#") or element.startswith("##")) or element.startswith("###") or element.startswith("####")]
    arrayOriginalFiltered = [element for element in arrayOriginal if not (element.startswith("#") or element.startswith("##")) or element.startswith("###") or element.startswith("####")]

    metadatas = getMetaDatas(arrayOriginalFiltered)

    print(len(arrayFiltered))
    arrayIds = [str(i) for i in range(len(arrayFiltered))]

    model = SentenceTransformer(getModelDefault())
    embeddings = model.encode(arrayFiltered)

    collection.add(
        documents=arrayFiltered,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=arrayIds,
    )

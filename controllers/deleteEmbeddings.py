import chromadb
import os
from utils.getRootPath import getRootPath
client = chromadb.PersistentClient(path=os.path.join(getRootPath(), 'data'))


def deleteCollection(nameCollection):
    client.delete_collection(nameCollection)
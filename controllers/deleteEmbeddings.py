import chromadb
client = chromadb.PersistentClient(path="../data")


def deleteCollection(nameCollection):
    client.delete_collection(nameCollection)
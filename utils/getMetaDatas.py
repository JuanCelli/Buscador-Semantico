from utils.splitTitles import splitTitles
from utils.splitContent import splitContent

def getMetaDatas(chunks):
    metadatas = [
        {
            "title": splitTitles(chunks[i]),
            "content": splitContent(chunks[i]),
        }
        for i in range(len(chunks))
    ]
    return metadatas
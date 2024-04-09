def splitContent(chunk):
    arrayContent = chunk.split("\n")[1:]
    content = '\n'.join(arrayContent)
    return content
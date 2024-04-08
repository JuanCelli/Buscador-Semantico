def openFileMd(url):
    with open(url, "r", encoding="utf-8") as archivo:
        return archivo.read()
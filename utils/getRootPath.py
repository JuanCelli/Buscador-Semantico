import os
def getRootPath():
    rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    return rootPath
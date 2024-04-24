import re
def splitFile(file):
    # Podemos colocar terminos que queremos reemplazar en el texto.
    # Ej: En este caso reemplazamos la palabra "COMPLETAR" con string vacio, podemos agregar más palabras o expresiones
    ignores = {
        "COMPLETAR":"",
    }

    for ignore, remplace in ignores.items():
        text = file.lower().replace(ignore.lower(),remplace)


    text = text.lower()

    chunks = re.split(r'### |#### |##  |#  ', text)
    chunks_originals= re.split(r'### |#### |##  |#  ', file)

    def format_text(chunk):
        return re.sub(r'\-\-\ ', '', chunk)

    result_text = [format_text(chunk) for chunk in chunks]

    return [[s.strip() for s in result_text if s.strip()],[s.strip() for s in chunks_originals if s.strip()]]
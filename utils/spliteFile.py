import re
def splitFile(file):
    ignores = {
        "COMPLETAR":"",
    }

    for ignore, remplace in ignores.items():
        text = file.lower().replace(ignore.lower(),remplace)


    text = text.lower()

    # chunks = re.findall(r'(#+ .+?)(?=\n#+ |\Z)', text, flags=re.DOTALL)
    chunks = re.split(r'### |#### |##  |#  ', text)

    def format_text(chunk):
        return re.sub(r'\-\-\ ', '', chunk)

    result_text = [format_text(chunk) for chunk in chunks]

    return [s.strip() for s in result_text if s.strip()]
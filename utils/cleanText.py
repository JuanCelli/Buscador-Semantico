import re
def cleanText(chunk):
    replace = {
        r'^#+\s+': '',  # Eliminar títulos (encabezados)
        r'\[.*?\]\(.*?\)': '',  # Eliminar enlaces
        r'^\d+\.\s+': '',  # Eliminar listas enumeradas
        r'^[\*\-+]\s+': '',  # Eliminar listas con viñetas
        r'(_{1,3}|\*{1,3})': '',  # Eliminar subrayado
        r'[\*_]+': '',# Eliminar cualquier formato restante
        r'\{\.mark\}|\{\.underline\}':"",
        r'\\':"",
        r'\n':"",
        r'\[|\]':"",
    }

    for ignore, replace in replace.items():
        text = re.sub(ignore, replace, chunk, flags=re.MULTILINE)
        texto_formateado = text.replace('\\n', '\n')
    
    return texto_formateado
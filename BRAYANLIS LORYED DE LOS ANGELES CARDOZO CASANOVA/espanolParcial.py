import re

archivo = "espanol.txt"

with open("espanol.txt", "r", encoding="utf-8") as f:
    texto = f.read()

# Expresiones regulares
enteros   = r"\b\d+\b(?!\.\d+)"   # enteros que no sean parte de decimales
flotante  = r"-?\b\d+\.\d+\b"     # decimales con punto (ej: 45.60)
listas    = r"(?i)\blista:\s*([a-záéíóúüñ,\s]+)\."  # lista: elemento1, elemento2.
palabras  = r"[A-Za-zÁÉÍÓÚáéíìóòúùÜüÑñ]+"           # palabras con acentos y ñ

# Conteos
resul_enteros  = re.findall(enteros, texto)
resul_float    = re.findall(flotante, texto)
resul_list     = re.findall(listas, texto)
resul_palabras = re.findall(palabras, texto, flags=re.IGNORECASE)

# Salida con el formato que pide el profe
print(f"{archivo}: {len(resul_palabras)} palabras, {len(resul_enteros)} enteros, {len(resul_float)} decimales, {len(resul_list)} listas")

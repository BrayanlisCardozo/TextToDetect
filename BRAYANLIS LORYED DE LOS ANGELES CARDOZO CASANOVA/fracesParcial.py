import re

archivo = "frances.txt"

with open("frances.txt", "r", encoding="utf-8") as f:
    texto = f.read()

enteros   = r"\b\d+\b(?!,\d+)"   # evita contar la parte entera de un decimal
flotante  = r"-?\b\d+,\d+\b"     # sigue con coma
listas    = r"(?i)\bliste:\s*([a-zàèéìòùç,\s]+)\."
palabras  = r"[A-Za-zÁÉÍÓÚáàéèíìóòúùÜüÑñç]+"

resul_enteros  = re.findall(enteros, texto)
resul_float    = re.findall(flotante, texto)
resul_list     = re.findall(listas, texto)
resul_palabras = re.findall(palabras, texto, flags=re.IGNORECASE)

print(f"{archivo}: {len(resul_palabras)} palabras, {len(resul_enteros)} enteros, {len(resul_float)} decimales, {len(resul_list)} listas")

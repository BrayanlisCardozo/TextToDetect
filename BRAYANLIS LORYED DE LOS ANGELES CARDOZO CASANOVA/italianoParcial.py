import re

archivo = "italiano.txt"

with open("italiano.txt", "r", encoding="utf-8") as f:
    texto = f.read()

# Regex ajustados
enteros   = r"\b\d+\b(?!,\d+)"   # evita contar la parte entera de un decimal
flotante  = r"-?\b\d+,\d+\b"     # decimales con coma
listas    = r"(?i)\blista:\s*([a-zàèéìòùáéíóúüñ,\s]+)\."
palabras  = r"[A-Za-zÁÉÍÓÚáàéèíìóòúùÜüÑñ]+"

# Buscar coincidencias
resul_enteros  = re.findall(enteros, texto)
resul_float    = re.findall(flotante, texto)
resul_list     = re.findall(listas, texto)
resul_palabras = re.findall(palabras, texto, flags=re.IGNORECASE)

# Imprimir resultado final
print(f"{archivo}: {len(resul_palabras)} palabras, {len(resul_enteros)} enteros, {len(resul_float)} decimales, {len(resul_list)} listas")



print("############## STRING METHODS ##############")


# string methods
print(f"'anartz' with upper() => '{'anartz'.upper()}'")

print(f"'replace()' function use with 'Ron Artest' to change'Artest' with 'World Peace' => {'Ron Artest'.replace('Artest', 'World Peace')}")

####################################
# How to figure things out in Python
####################################
print("############## FIGURE THINGS OUT ##############")
print('Documentación de str: https://docs.python.org/3/library/string.html')

print(f"Uso de 'capitalize() con 'lebron james': {'lebron james'.capitalize()}")
print(f"Uso de 'isalpha() con 'lebron james': {'lebron james'.isalpha()}")

print(f"Uso de 'encode() con 'lebron james': {'lebron james'.encode()}")
print(f"Uso de 'isidentifier() con 'lebron james': {'lebron james'.isidentifier()}")
print(f"Uso de 'casefold() con 'lebron james': {'lebron james'.casefold()}")
print(f"Uso de 'isascii() con 'lebron james': {'lebron james'.isascii()}")
print(f"Uso de 'format() con 'lebron james': {'lebron james'.format()}")
print(f"Uso de 'isspace() con 'lebron james': {'lebron james'.isspace()}")
print(f"Uso de 'endswith('es') con 'lebron james': {'lebron james'.endswith('es')}")
print(f"Uso de 'islower() con 'lebron james': {'lebron james'.islower()}")


print("############## ESPACIOS con STR ##############")
# Texto original
text = "   lebron    james   "

# 1️⃣ Eliminar espacios al inicio y al final
clean_strip = text.strip()
print(f"Strip (inicio y fin): '{clean_strip}'")

# 2️⃣ Eliminar todos los espacios de la cadena
clean_no_spaces = text.replace(" ", "")
print(f"Replace (todos los espacios): '{clean_no_spaces}'")

# 3️⃣ Eliminar espacios extra dejando solo uno entre palabras
clean_normalized = " ".join(text.split())
print(f"Normalized (solo un espacio entre palabras): '{clean_normalized}'")

# 4️⃣ Usando expresiones regulares para controlar espacios
import re
clean_regex = re.sub(r"\s+", " ", text).strip()
print(f"Regex (espacios múltiples a uno, strip al inicio y fin): '{clean_regex}'")

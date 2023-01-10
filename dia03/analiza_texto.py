texto = input("Introduzca un texto: ")

letras = input("Introzuzca 3 letras separadas por ,: ").lower()

letras = letras.split(",")

print(f"La letra {letras[0]} aparece {texto.lower().count(letras[0])}")
print(f"La letra {letras[1]} aparece {texto.lower().count(letras[1])}")
print(f"La letra {letras[2]} aparece {texto.lower().count(letras[2])}")

print(f"En total el texto tiene {len(texto.split())} palabras.")
print(f"La primera letra del texto es {texto[0]} y la última es {texto[len(texto)-1]}")

print(texto[::-1])

if "python" in texto:
    print("La palabra python se encuentra")
else: 
    print("La palabra python NO se encuentra")
print(25 == 5**0.5)
letras = []
print("Ingreas una frase")
frase = "Xab caa msmibz"
frase_upper = frase.upper()
print("Suministra la informacion")
print("Ingresa una letra")
letras.append(input())
print("Ingresa la segunda letra")
letras.append(input())
print("Ingresa la tercera letra")
letras.append(input())

print(f"Resultados:\nCantidad de letras en la Frase")
print(f"La letra {letras[0].upper()} aparece: {frase_upper.count(letras[0].upper())} veces.")
print(f"La letra {letras[1].upper()} aparece: {frase_upper.count(letras[1].upper())} veces.")
print(f"La letra {letras[2].upper()} aparece: {frase_upper.count(letras[2].upper())} veces.")

print(f"La Frase que ingresaste tiene {len(frase.split())} palabras")

print(f"La primera letra de la Frase es: {frase[0].upper()}")
print(f"La ultima letra de la Frase es: {frase[-1].upper()}")
frase_invertida = frase_upper.split()
frase_invertida.reverse()
frase_invertida = " ".join(frase_invertida)

print(f"Las palabras invertidas quedan de esta manera:\n{frase_invertida}")
print("Python" in frase)

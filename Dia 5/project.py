from random import *
texto = "unción principal indicar que en la lectura se debe hacer una pausa: es indistinta su función a la hora de realizar una lectura en voz alta"
letras = []
es_ganador = False
intentos = 0
vida = randint(4,8)
def elegir_palabra (texto):
    palabras = texto.split(' ')
    palabra = choice(palabras)
    return palabra
def error_message (error):
    match error:
        case 1:
            return "❌ UPSS..!!!\nFavor Ingrese una Letra"
        case 2:
            return "❌ UPSS..!!!\nSolo Debe Ingresar una Letra"
        case 3:
            return "❌ UPSS..!!!\nDebe Ingresar una Letra"
        case 4:
            return "❌ UPSS..!!!\nLetra ya seleccionada"
        case 5:
            return "❌ UPSS..!!!\nLetra Incorrecta"
        case _:
            return "❌ UPSS..!!!\nError no Encontrado"
def letra_ingresada(letra, lista_letras, palabra_random):
    if not letra.isalpha():
        return 1
    if len(letra) > 1:
        return 2
    if not letra:
        return 3
    if lista_letras.count(letra):
        return 4
    if not palabra_random.count(letra):
        return 5
    return 0
def armar_string(letras,palabra):
    # palabra =''
    letras =''.join(letras).lower()
    palabra_final = palabra
    for letra in palabra:
        if letras.count(letra) == 0 :
            palabra_final = palabra_final.replace(letra,'_')

    return palabra_final.upper()

def mensaje_final (es_ganador, resultado):
    mensaje = ""
    if es_ganador :
        mensaje = "\n--- FELICIDADES --- \n😁😁😁Ganaste!!!😁😁😁"
    else:
        mensaje = "\n--- INTENTALO DE NUEVO 😓 ---"
    mensaje += "\nTú Resultado:" + resultado

    mensaje += "\n\n--- END GAME ---"
    return mensaje



palabra = elegir_palabra(texto)
print(palabra)


print("\n--- START GAME  ---\n")
print(f"Bienvenido a El Ahorcado")
print(f"--- Detalles ---\n1.Cuentas con {vida} vidas ❤️\n2.La Palabra cuenta {len(palabra)} con letras")
while vida > 0:
    intentos += 1
    palabra_final = armar_string(letras,palabra)
    if palabra_final.count('_') == 0:
        es_ganador = True
        break
    print(f"\n--- Intento:{intentos} ❤️: {vida} ---\n{palabra_final}")
    letra = input("Ingresa una letra:\n")
    validacion = letra_ingresada(letra,letras,palabra)

    if validacion != 0 and validacion != 1:
        print(f'{error_message(validacion)}')
        vida -= 1
    else:
        print("✅ CORRECTO!!!")

    letras.append(letra)

print(mensaje_final(es_ganador,palabra_final))
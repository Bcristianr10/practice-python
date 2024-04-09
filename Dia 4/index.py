from random import *
message = {
    'fuera_rango':'Ha elegido un número que no está permitido',
    'menor':'Su respuesta es incorrecta y que ha elegido \nun número menor al número secreto',
    'mayor':' Su respuesta es incorrecta y que ha elegido \nun número mayor al número secreto',
    'acertado':'Has ganado',
}
data = {
    'rango_inicial':randint(1,10),
    'rango_final':randint(11,100),
    'intentos':randint(1,10)
}
data['numero_final'] = randint(data['rango_inicial'],data['rango_final'])

print("\n--- START GAME ---\n")
print("Bienvenido a Adivina el Número")
nombre_jugador = input("1. Ingresa tú nombre\n")
print(f"Bueno, {nombre_jugador}, he pensado un número entre {data['rango_inicial']} y {data['rango_final']}, \ny tienes solo {data['intentos']} intentos para adivinar cuál crees\nque es el número\n \n--- Empecemos ---")
intentos = 0
while intentos < data['intentos']:
    intentos += 1
    print(f"\nIntento {intentos} de {data['intentos']}")
    entrada = 0
    while entrada < 1:
        eleccion = input("Dígita un número: \n")
        if eleccion.isnumeric() :
            entrada = 1
            continue
        print("- Upss..! Debe ingresar un valor númerico")
    eleccion = int(eleccion)

    if eleccion < data['rango_inicial'] or eleccion > data['rango_final']:
        print("Respuesta: "+message['fuera_rango'])
        continue
    if eleccion < data['numero_final']:
        print("Respuesta: "+ message['menor'])
        continue
    if eleccion > data['numero_final']:
        print("Respuesta: "+ message['mayor'])
        continue
    if eleccion == data['numero_final']:
        print(f"Respuesta: {message['acertado']} en {intentos} {'intento' if  intentos == 1 else 'intentos'}")
        break

if eleccion != data['numero_final'] and intentos == data['intentos']:
    print('\nHAS FALLADO VUELVE A INTENTARLO')
else:
    print("--- FELICIDADES ---")
print("\n--- END GAME ---")

# data = {'rango_inicial':randint(1,10),'rango_final':randint(11,100),'intentos':randint(1,10)}
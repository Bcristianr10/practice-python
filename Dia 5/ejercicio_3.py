def evaluar_cero (*args):

    numero_anterior = False
    for numero in args:
        if numero == 0 and numero_anterior == numero:
            return True
        numero_anterior = numero
    return False

print(evaluar_cero(1,2,3,4,0,3,0,2,0,0,5,0,5))
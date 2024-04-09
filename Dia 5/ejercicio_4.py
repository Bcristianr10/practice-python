def contar_primos(*args):
    for numero in args:
        es_par = False
        if numero > 1:
            for num in range(numero):
                if num > 1 :
                    if es_par:
                        break
                    if numero%num == 0:
                        es_par = True
            if not es_par:
                print(numero)
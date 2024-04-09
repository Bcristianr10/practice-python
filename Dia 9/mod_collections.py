from collections import Counter, defaultdict, namedtuple, deque
numeros  = [8,1,5,1,8,6,12,5,5,1,4,5]
frase = 'al pan pan y al vino vino'

# Contar
print(Counter(numeros))
print(Counter(frase.split()))
print(Counter('mississippi'))

# Asignamos nada cuando no existe
mi_dic = defaultdict(lambda: 'nada')
mi_dic['uno'] = 'verde'
print(mi_dic['dos'])

# Practicamente es crear un objeto tipado o una clase
Persona = namedtuple('persona',['nombre','altura','peso'])
ariel = Persona('Ariel',1.76,79)
print(ariel.altura)



lista = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]
lista_ciudades = deque(lista)
lista_ciudades.appendleft('sss')
print(lista_ciudades)
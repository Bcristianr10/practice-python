import os
from pathlib import Path
from os import system
categoria_receta = []
recetas = []
data = {
    'menu_principal':['Leer Receta','Crear Receta','Crear Categoría','Eliminar Receta','Eliminar Categoría'],
    'menu_activo':'menu_principal',
    'acciones':[],
    'error':''
}
estado = 0
lista_errores ={
    'validar_numero':'Ingrese un Número ',
    'numero_invalido':'Número Invalido, debe ser del 1 al 6'
}
base = Path(Path.home(),'documents','test','Recetas')

# Obtener las categorias de las carpetas
def obtener_categoria():
    for rr in Path(base).glob('*'):
        categoria_receta.append(rr.stem)

def obtener_recetas():
    base_categoria = Path(base,data['acciones'][1])
    for rr in Path(base_categoria).glob('*'):
        recetas.append(rr.stem)

def validar_entrada(eleccion, cantidad = 5):
    if not eleccion.isnumeric():
        return 1
    eleccion = int(eleccion)
    if eleccion < 0 or eleccion > cantidad:
        return 2
    return eleccion

def print_menu (titulo,lista_menu):

    print(f'--- {titulo} ---')
    for key,categoria in enumerate(lista_menu):
        print(f'{key + 1}. {categoria}')


def void():
    match data['menu_activo']:
        case 'menu_principal':
            print_menu('Menu Principal',data['menu_principal'])
        case 'categorias':
            print_menu('Categoria de Recetas', categoria_receta)
        case 'recetas':
            print_menu('Categoria de Recetas', recetas)

    print('0. Salir')
    if data['error']:
        print(f'Error: {lista_errores[data["error"]]}\n')
    else:
        print()

def entrada ():
    eleccion = input("Elección: ")
    system('cls')
    return validar_entrada(eleccion)

def recibir_parametros():
    data['error'] = ''
    eleccion = entrada()
    match eleccion:
        case 1:
            data['error'] = 'validar_numero'
        case 2:
            data['error'] = 'numero_invalido'
    # system("cls")
    if data['menu_activo'] =='menu_principal':
        if int(eleccion) in (1,2,4,5):
            data['menu_activo'] = 'categorias'
        data['acciones'].append(data['menu_principal'][eleccion - 1])
        match int(eleccion):
            case 0:
                return 1
    elif data['menu_activo'] == 'recetas':
        data['acciones'].append(recetas[eleccion - 1])
    else:
        data['menu_activo'] = 'recetas'
        data['acciones'].append(categoria_receta[eleccion - 1])
        # print(data['acciones'])
        obtener_recetas()

    if data['menu_activo'] == 'recetas' and len(data['acciones']) == 3:
        ruta_base = Path(base, data['acciones'][1])
        print()
        data['menu_activo'] = 'none'
        if data['acciones'][0].find('Leer') == 0:
            print('--- Detalles de la Receta ---')
            print(Path(base, ruta_base, recetas[eleccion - 1] + '.txt').read_text())
        if data['acciones'][0].find('Crear Receta') == 0:
            nombre_receta = input('Nombre de la Receta\n')
            contenido_receta = input('Cotenido de la Receta\n')
            file = open(Path(ruta_base,nombre_receta + '.txt'),'w')
            file.write(contenido_receta)
            file.close()
        if data['acciones'][0].find('Eliminar Receta') == 0:
            if Path(base, ruta_base, recetas[eleccion - 1] + '.txt').exists():
                os.remove(Path(base, ruta_base, recetas[eleccion - 1] + '.txt'))

        if data['acciones'][0].find('Eliminar Categoría') == 0:
            print('entre')
            if list(Path(ruta_base).glob('*')) :
                print('No es posible eliminar, contiene recetas')
            else:
                os.rmdir(ruta_base)
                print('Eliminado')


    if data['acciones'][0].find('Crear Categoría') == 0:
        nombre_categoria = input('Nombre de la Categoría\n')
        os.makedirs(Path(base, nombre_categoria))

    return 0
    # continue


obtener_categoria()
while estado == 0:
    void()
    estado = recibir_parametros()







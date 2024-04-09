class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
class Cliente(Persona):
    def __init__(self,nombre,apellido,cuenta,balance):
        super().__init__(nombre,apellido)
        self.cuenta = int(cuenta)
        self.balance = int(balance)



    def imprimir_data(self):
        print(f"--- Detalles de la Cuenta ---\nNombre: {self.nombre +' '+ self.apellido} \nCuenta: {self.cuenta} \nBalance: {self.balance} dolares")

    def depositar(self):
        print(f'--- Depositar a la cuenta: {self.cuenta}')
        monto = int(input('Monto a Depositar:\n'))
        self.balance += monto
        print(f'Se depositaron {monto} dolares')


    def retirar(self):
        print(f'--- Retirar de la cuenta: {self.cuenta}')
        monto = int(input('Monto a Retirar:\n'))
        if monto <= self.balance:
            self.balance -= monto
            print(f'Se retiraron {monto} dolares')
        else:
            print(f'No puedes retirar {monto} porque es mayor a tu saldo de: {self.balance}')


def menu ():
    menus = ['Informacion','Depositar','Retirar']
    print('\n--- Menu ---')
    for key,menu in enumerate(menus):
        print(f'{key + 1}. {menu}')
    # print('\n')

def crear_cliente(data):
    return Cliente(data['nombre'],data['apellido'],data['cuenta'],data['balance'])

def inicio():
    print('Cuenta Bancaria \n\nNuevo Usuario')
    data = {}
    data['nombre'] = input('Nombre: ')
    data['apellido'] = input('Apellido: ')
    data['cuenta'] = input('Cuenta: ')
    data['balance'] = input('Balance: ')
    nuevo_cliente = crear_cliente(data)
    nuevo_cliente.imprimir_data()
    estado = 0
    while estado == 0:
        menu()
        match int(input('Elección: ')):
            case 1:
                nuevo_cliente.imprimir_data()
            case 2:
                nuevo_cliente.depositar()
            case 3:
                nuevo_cliente.retirar()






# cliente = Cliente("Mario",'p','c','b')

inicio()
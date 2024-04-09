print("Ingrese su nombre")
nombre = input()
print("Cuanto vendido en este mes")
venta = input()

comision = round(int(venta) * 0.13,2)

print(f"Hola, {nombre} tus comisiones son: {comision}")
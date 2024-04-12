from datetime import time,datetime,date

#mi_hora = datetime.time(17,35)
#dia = datetime

#print(dia.today())
#print(type(mi_hora),mi_hora, dia.today())


hoy = datetime.today().date()

print(hoy)

minutos = datetime.today().time().minute

print(minutos)
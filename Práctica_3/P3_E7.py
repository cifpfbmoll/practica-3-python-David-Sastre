# Pida al usuario tres número que serán el día, mes y año. /
# Comprueba que la fecha introducida es válida.  Por ejemplo:
# 32/01/2017->Fecha incorrecta
# 29/02/2017->Fecha incorrecta
# 30/09/2017->Fecha correcta.
# Tienen 31 días: Enero, marzo, mayo, julio, agosto, octubre y diciembre.
# Tienen 30 días: Abril, junio, septiembre y noviembre.
# Tienen 28 días: Febrero.

day = int(input("Digame un dia: "))
month = int(input("Digame un mes: "))
year = int(input("Digame un año: "))

if (day==31 and month==4 or month==6 or month==9 or month==11):
    print("Fecha invalida")
elif(day>=29 and (month==2)):
    print("Fecha invalida")
elif(month>12):
    print("Fecha invalida")
else:
    print ("Fecha correcta")

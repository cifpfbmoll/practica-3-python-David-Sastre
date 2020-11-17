# Pida un número que como máximo tenga tres cifras /
# (por ejemplo serían válidos 1, 99 i 213 pero no 1001). /
# Si el usuario introduce un número de más de tres cifras debe un informar/
#  con un mensaje de error como este /
# "ERROR: El número 1005 tiene más de tres cifras"

print("Por favor introduce un n�mero de tres cifras")
num=int(input())
if  num > 999:
    print("ERROR el n�mero", num,"tiene m�s de tres cifras")
else:
    print(num)

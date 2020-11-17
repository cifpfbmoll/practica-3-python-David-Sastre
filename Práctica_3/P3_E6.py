# Pida al usuario el precio de un producto y el nombre del producto y muestre\
#el mensaje con el precio del IVA (21%).Por ejemplo: "Tu bicicleta vale \
#100 euros y con el 21 % de IVA se queda en 121 euros en total."
print("Introduce el nombre de un producto")
prod=input()
print("Introduce el valor del producto sin iva")
p=float(input())
pf=((p*0.21)+p)
print("Tu", prod, "vale", p,"euros y con el 21% de IVA se queda en",pf,"euros en total")
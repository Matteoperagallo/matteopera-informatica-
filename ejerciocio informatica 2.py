a = input("ingresa el valor de a: ")
b = input ("ingrese el valor de b: ")

print(f"antes del intercambio: a = {a},{b}")

a,b = b,a 
print(f"despues del intercambio:a = {a},b = {b}")

a,b = b,a 
print(f"despues del intercambio:a = {a},b = {b}:")
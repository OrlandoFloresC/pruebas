#video #20 programacion ats

#capitulo 2, condicionales

# ejercicio 7: hacer un programa que determine cual es el mayor de tres numeros

a = 5 #float(intput("Ingrese un valor: "))
b = 5 #float(intput("Ingrese un valor: "))
c = 5 #float(intput("Ingrese un valor: "))

if a >= b and a >= c:
    print(f"El valor {a} es mayor")

elif b >= a and b >= c:
    print(f"El valor {b} es mayor")

elif c >= a and c >= b:
    print(f"El valor {c} es mayor")
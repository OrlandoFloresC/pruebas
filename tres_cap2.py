#video #20 programacion ats

#capitulo 2, condicionales combinados

# ejercicio 6: hacer u8n programa que pida dos numeros y se de cuenta
#cual de ellos es par o si ambos lo som

a = 5 #float(input("Digite un numero: "))
b = 5 #float(input("Digite un numero: "))

if a % 2 == 0 and b % 2 ==0:
    print("ambos son pares")

elif a % 2 == 0 and b % 2 !=0:
    print("El numero uno es par")

elif a % 2 != 0 and b % 2 ==0:
    print("El numero dos es par")

else:
    print("Ambos son impares")



#video #23 programacion ats

#capitulo 2, condicionales

# ejercicio 10: hacer un programa que simule un cajero automatico con un saldo inicial de 1000
# y tendra el siguiente  menu de opciones:
#1.- ingresar dinero en cuenta
#2.- retirar dinero de la cuenta
#3.- mostrar dinerop disponible. 
#4.- salir

print("Bienvenido\nUsted cuenta con 1000 pesos en cuenta")
print("Que operacion desea realizar")
print("1.- ingresar dinero en cuenta")
print("2.- retirar dinero de cuenta")
print("3.- mostrar dinero en cuenta")
print("4.- salir")
dinero = 1000

respuesta = input("Presiona el numero de la operacion deseada: ")
if respuesta == "1":
    ingresar = float(input("Digite la cantidad: "))
    cantidad = dinero + ingresar
    x = input("3.- mostrar dinero en cuenta: ")
    if x == "3":
        print(f"El dinero en la cuenta es {cantidad}")
    else:
        print(" ")

elif respuesta == "2":
    retirar = float(input("Digite la cantidad: "))
    cantidad = dinero - retirar
    x = input("3.- mostrar dinero en cuenta: ")
    if x == "3":
        print(f"El dinero en la cuenta es {cantidad}")
    else:
        print(" ")

elif respuesta == "3":
    print(f"El dinero en la cuenta es {dinero}")

elif respuesta == "4":
    print(f" ")






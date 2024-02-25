#video #22 programacion ats

#capitulo 2, condicionales

# ejercicio 9: construir un programa que simule el funcionamiento
# de una caqlculadora que puede realizar las cuatro operaciones 
#aritmeticas basicas

print("Este programa es una calculadora------\nA continuacion selecciona la operacion que deseas\ns = suma, r = resta, m = multiplicasion, d = divicion")
seleccion = input("Seleeciona la opracion a realizar: ").upper()



if seleccion == "S" or seleccion == "R" or seleccion == "M" or seleccion == "D":
    Num1 = float(input("Ingresa el primer valor: "))
    Num2 = float(input("Ingresa el segundo valor: "))
    if seleccion == "s":
        suma = Num2 + Num1
        print (f"El resultado de la suma es {suma:.2f}")

    elif seleccion == "r":
        resta = Num1 - Num2
        print (f"El resultado de la resta es {resta:.2f}")

    elif seleccion == "m":
        mult = Num1 * Num2
        print (f"El resultado de la multiplicasion es {mult:.2f}")

    else:
        div = Num1 / Num2
        print (f"El resultado de la division es {div:.2f}")

else:
    print (f"El valor ingresado no esta en la memoria\nReinicia el programa")
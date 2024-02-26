#video #34 programacion ats

#capitulo 3: colecciones

#ejercicio 1: escribe un programa donde tenga una lista y que
#a continuacion, elimine los elementos repetidos, 
#pot ultimo mosdtrar la lista

lista =[1,2,3,4,5,6,3,23,6,7,8,9,10]
print(lista)
conjunto = set(lista)
print(conjunto)
lista = list(conjunto)
print(lista)

#otra manera
lista =[1,2,3,4,5,6,3,23,6,7,8,9,10]
print(lista)
lista = list(set(lista))
print(lista)
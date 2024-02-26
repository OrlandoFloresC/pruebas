#video #26 programacion ats

#capitulo 3, listas (colecciones)
lista = [1,2,3,4,5]
lista.append(6) #agrega al final
lista.append(8) #agrega al final
lista.insert(6,7)   #agrega en una posicion determianda(indice, valor)
lista.extend([9,10])  #agrega toda una lista
lista2 = [11,12,13]
lista3 = lista + lista2 #hace lo mismo q extend

print (3 in lista) #busca si hay un valor en la lista
print (11 in lista)
print (lista.index(5))  #devuelve el indice de lo q buscas
print(lista.count(1))   #cuenta cuantas veces hay un valor en a lista

print (lista3)
print(lista)
lista.pop() #si la dejamos vacia. elimina el ultimo valor de la lista
lista.pop(8) # se le da el indice
print(lista)
lista.remove(8) # elimina el valo que agregaos. es para cuando no sabemos el indice
lista.reverse()#reversea toda la lista en el orden en que este
print(lista)
lista.sort() #ordena de m,enor a mayor
print(lista)
lista.sort(reverse=True) #ordena de mayor a  menor
print(lista)
lista.clear() #deja vacia la lista
print(lista)
#video #28 programacion ats

#capitulo 3: conjuntos (los elementos se agregan desordenados) no puede haber repetidos

conjunto = set()  #debe llevar el set

conjunto = {1,2,3,4,"Hola",4.5,3}     #para que sea un conjunto se hace con las llaves, si no tiene set es un diccionario
#no puede haber otro tipo de coleccion adentro
conjunto.add(6)
conjunto.add(100)
conjunto.add("si")
print (conjunto)
conjunto.discard("Hola")
print (conjunto)
print (3 in conjunto)
print (3 not in conjunto)
conjunto.clear()
print (conjunto)
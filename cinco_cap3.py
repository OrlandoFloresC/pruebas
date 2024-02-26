#video #29 programacion ats

#capitulo 3: conjuntos

a = {1,2,3}
b = {3,1,2}
d = {3,4,5,6}
j = frozenset({1,2,3,4,5,6,7,8,9,10}) #con frosenset se hace inmutable
c = a| b #union
e = a| d  #union
f = a & b #interseccoin
g = a & d  #interseccion
h = a-d #diferencia
i = a ^ b #difrencia simetrica 


print (c)
print (e)
print (f)
print (g)
print (h)
print (i)
print (a.issubset(j)) #preguntando si a es un sub conjunto de j
print (j.issuperset(a)) #conjunto potencia
print (a.isdisjoint(b)) #disconexo
print(a == b)
print(len(a))
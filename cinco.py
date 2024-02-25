#video #8
#operadores logicos

# perimte contruir expreciones logiacas, 
#se obtiene como resultado booleanos

# And   "conjuncion"  and
#Or      "disyuncion"  or
# negacion             not

# and multiplicacion lojica
#or suma logica 
#not           

""" orden de evalucion

1.- not
2.- and
3.- or
"""        
a = 10
b = 12 
c = 13
d = 10
resultado = ((a>b)or(a<c))and((a==c)or(a>=b))
print(resultado)

e =10
f = 15
g = 20

resultado = ((a>b)or(b<c))
print(resultado)
resultado = ((a>b)and (b<c))
print(resultado)
resultado = not((a>b) and (b<c))
print(resultado)
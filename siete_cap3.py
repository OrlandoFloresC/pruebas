#video #31 programacion ats

#capitulo 3: diccionarios

equipo = {10:"paulo", 11:"douglas", 7:"cristiano",17:"mario"}
print(equipo[10]) #aqui lo q se agrega es clave, y no indice
print(equipo.get(11, "No existe un jugador con esa camiseta"))
print(10 in equipo)
print(20 in equipo)
print(equipo.keys())
print(equipo.values())
print(equipo.items())
print(len(equipo))
equipo.clear()
print(equipo)
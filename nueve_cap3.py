#video #33 programacion ats

#capitulo 3: colas(el primero en llegar es el primero en salir)

cola = ["maria", "jose", "juan", "pancho"]
print(cola)
#agregamos elementos al final de  la cola
cola.append("carla")
cola.append("diana")
print(cola)
#sacando elemtos por el principio de la cola
n = cola.pop(0)
print(f"Estan atendiendo a {n}")
print(cola)

for i in cola:
    n = cola.pop(0)
    print(f"Estan atendiendo a {n}")
    print(cola)
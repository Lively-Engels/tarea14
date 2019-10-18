from random import randrange
def aleatorios():
    lista = []
    for i in range (0,10000):
        lista.append(randrange(0,100))
    return lista

def busca(lista):
    repetido=0
    bus=[]
    j=int(input("¿Cuantos numeros desea buscar? "))
    for i in range (0,j):
       bus.append(int(input(f"{i}.- ¿Que numero desea buscar? "))) 
    for i in range (0,j):
        repetido=0
        for x in range (0,len(lista)):
            if (bus[i]==lista[x]):
                repetido = repetido+1
            else:
                repetido=repetido
        print(f"El numero {bus[i]} se repitio: {repetido} veces")

lista=aleatorios()
print(f"")


#ACTIVIDA 9
cliente={}
def lugares(clientes):
    if len(clientes)==0:
        return 0
    cliente=clientes[0]
    return len(clientes[cliente]["destinos"])+lugares(clientes[1:])

def maximo(clientes):
    max=-1
    clientemax=""
    for codigo, informacion in clientes.items():
        cantidad = len(informacion["destinos"])
        if cantidad>max:
            max=cantidad
            clientemax= informacion["nombre"]
    return clientemax, max

n=int(input("INgrese ek numero de clinetes"))

for i in range(n):
    print(f"clienyte {i+1}")
    codigo = input("ingrese el codigo del cliente")
    nombre= input("imgrese el nombre del cliente")

while True:
    visitas= int(input("Ingrese numeero de visitas, maximo 5"))
    if 1<= visitas<=5:
        break
    print("error, solo numeros del 1-5")

destinos=[]
for j in range(visitas):
    destino=input(f"destino{j+1}")
    destinos.append(destino)
clientes[codigo]={
        "nombre": nombre,
        "destinos": destinos
    }

#ACTIVIDA 9
cliente={}
def lugares(clientes):
    if len(clientes)==0:
        return 0
    cliente=clientes[0]
    return len(cliente[cliente]["destinos"])+lugares(clientes[1:])

def maximo(clientes):
    max
print("Ingrese numeero de clientes")

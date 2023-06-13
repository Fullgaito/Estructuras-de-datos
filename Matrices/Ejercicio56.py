"""2. Leer una matriz de n filas por 12 columnas. Cada elemento contiene el valor de las ventas
de cada uno de los n vendedores de una compañía para cada uno de los 12 meses del año.
Se debe calcular: El total de ventas para cada vendedor en el año, el total de ventas para
cada mes y total de ventas de toda la compañía."""

meses={1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"Noviembre",12:"Diciembre"}
def LeerMatriz():
    n=int(input("Digite el numero de filas: "))
    
    fila=[]
    matriz=[]
   
    for i in range(n):
        for j in range(12):
            a=int(input(f"Digite las ventas de {meses[j+1]} del trabajador {i+1}: "))
            fila.append(a)
        matriz.append(fila)
        fila=[]
    return matriz
A=LeerMatriz()
#Total de ventas para cada vendedor en el año
suma=0
for k in range(len(A)):
    for m in A[k]:
        suma+=m
    print(f"El total de ventas para el trabajador {k+1} es:${suma}")
    suma=0
#total de ventas para cada mes
mes=0
total=0
for w in range(12):
    for u in A:
        a=u[w]
        mes+=a
        total+=a
    print(f"El total de ventas para {meses[w+1]} es:{mes}")
    mes=0
print(f"El total de ventas de la compañia es de ${total}")

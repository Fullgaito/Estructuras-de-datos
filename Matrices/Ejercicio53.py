"""4. Realizar un algoritmo que lea una matriz, calcule y escriba la suma de los elementos de
la primera fila y el producto de los elementos de la última columna. Escribir la matriz
original."""

def LeerMatriz():
    n=int(input("Digite el numero de filas: "))
    m=int(input("Digite el numero de columnas:" ))

    fila=[]
    matriz=[]

    for i in range(n):
        for j in range(m):
            a=int(input(f"Digite el elemento {j+1} de la fila {i+1}: "))
            fila.append(a)
        matriz.append(fila)
        fila=[]
    return matriz
A=LeerMatriz()

#suma primer fila
suma=0
for m in A[0]:
    suma+=m
print(f"La suma es:{suma}")
#producto ultima columna
producto=1
for u in A:
    a=u[-1]
    producto*=a
print(f"El producto es:{producto}")
print("La matriz original es:")
for t in A:
    print(t)



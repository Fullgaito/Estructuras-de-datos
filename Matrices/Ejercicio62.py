"""3. Leer una matriz cuadrada, generar un vector con la diagonal principal."""

def LeerMatriz():
    n=int(input("Digite el numero de filas: "))
    m=int(input("Digite el numero de columnas:" ))

    fila=[]
    matriz=[]
    while n!=m:
        print("las filas deben ser iguales a las columnas")
        n=int(input("Digite el numero de filas: "))
        m=int(input("Digite el numero de columnas:" ))

    for i in range(n):
        for j in range(m):
            a=int(input(f"Digite el elemento {j+1} de la fila {i+1}: "))
            fila.append(a)
        matriz.append(fila)
        fila=[]
    return matriz
A=LeerMatriz()
v=[]
for m in range(len(A)):
    for w in range(len(A)):
        if m==w:
            v.append(A[m][w])
print(A)
print(v)
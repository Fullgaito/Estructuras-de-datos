"""1.Realizar un algoritmo que lea 2 matrices. Calcular y escribir una nueva matriz que sea la
suma de estas matrices."""

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
B=LeerMatriz()

#suma
resultante=[]
f=[]
for m in range(len(A)):
    for r in range(len(B)):
        b=A[m][r]+B[m][r]
        f.append(b)
    resultante.append(f)
    f=[]
for t in resultante:
    print(t)

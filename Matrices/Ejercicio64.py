"""5. Leer una matriz cuadrada de orden 2 o 3. Calcular y escribir su determinante."""

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

if len(A)==2:
    det=(A[0][0]*A[1][1])-(A[0][1]*A[1][0])
    print(f"El determinante es:{det}")
elif len(A)==3:
    #aplicar Ley de sarrus
    f1=A[0]
    f2=A[1]
    A.append(f1)
    A.append(f2)
    det1=A[0][0]*A[1][1]*A[2][2]+A[1][0]*A[2][1]*A[3][2]+A[2][0]*A[3][1]*A[4][2]
    det2=A[0][2]*A[1][1]*A[2][0]+A[1][2]*A[2][1]*A[3][0]+A[2][2]*A[3][1]*A[4][0]
    det=det1-det2
    print(f"El determinante es:{det}")
else:
    print("No es 2 ni 3")
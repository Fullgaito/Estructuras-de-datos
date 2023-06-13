class Nodo:
  def __init__(self,dato):
    self.dato=dato
    self.siguiente=None
class ListaEnlazada:
    def __init__(self):
        self.cabeza=None
    def insertar(self, dato):
        NuevoNodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = NuevoNodo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = NuevoNodo
    def Duplicados(nueva):
        valores = {}
        actual = nueva.cabeza
        siguientenodo = None
        while actual:
            if actual.dato in valores:
                siguientenodo.siguiente = actual.siguiente
            else:
                valores[actual.dato] = True
                siguientenodo = actual
            actual = actual.siguiente
    

n=ListaEnlazada()
n.insertar(2)
n.insertar(3)
n.insertar(2)
n.insertar(3)
ListaEnlazada.Duplicados(n)
class Nodo:
    def _init_(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

class ListaEnlazada:
    def _init_(self):
        self.cabeza = None
        self.tamaño = 0

    def _len_(self):
        return self.tamaño

    def insertar(self, dato, k):
        if k < 0 or k > self.tamaño:
            raise ValueError("Posición inválida")
        nuevo_nodo = Nodo(dato)
        if k == 0:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            anterior = self._get_nodo(k-1)
            nuevo_nodo.siguiente = anterior.siguiente
            anterior.siguiente = nuevo_nodo
        self.tamaño += 1

    def eliminar(self, k):
        if k < 0 or k >= self.tamaño:
            raise ValueError("Posición inválida")
        if k == 0:
            nodo_eliminado = self.cabeza
            self.cabeza = self.cabeza.siguiente
        else:
            anterior = self._get_nodo(k-1)
            nodo_eliminado = anterior.siguiente
            anterior.siguiente = nodo_eliminado.siguiente
        self.tamaño -= 1
        return nodo_eliminado.dato

    def contar(self, valor):
        contador = 0
        actual = self.cabeza
        while actual:
            if actual.dato == valor:
                contador += 1
            actual = actual.siguiente
        return contador

    def _get_nodo(self, k):
        nodo_actual = self.cabeza
        for i in range(k):
            nodo_actual = nodo_actual.siguiente
        return nodo_actual
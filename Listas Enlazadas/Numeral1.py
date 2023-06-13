class Nodo:
  def __init__(self,dato):
    self.dato=dato
    self.siguiente=None

class ListaEnlazada:
  def __init__(self):
    self.cabeza=None
  #Retorne el tamaño de la lista
  def Tamano(self):
        nodoA = self.cabeza
        tam = 0
        while nodoA:
            tam += 1
            nodoA = nodoA.siguiente
        return tam
  #Inserte un elemento en la posicion k
  def insertar_en_posicion(self, dato, k):
      nuevo_nodo = Nodo(dato)
        
      if self.cabeza is None:
          self.cabeza = nuevo_nodo
          return
        
      if k == 0:
          nuevo_nodo.siguiente = self.cabeza
          self.cabeza = nuevo_nodo
          return
        
      actual = self.cabeza
      previo = None
      i = 0
        
      while i < k and actual is not None:
          previo = actual
          actual = actual.siguiente
          i += 1
        
      if actual is None:
          previo.siguiente = nuevo_nodo
          return
        
      previo.siguiente = nuevo_nodo
      nuevo_nodo.siguiente = actual
  #elimine un elemento de la posicion k
  def borrarPosicion(self,pos):
    anterior=self.cabeza
    actual=self.cabeza
    k=0
    if pos>0:
      while k!=pos and actual.siguiente!=None:
        anterior=actual
        actual=actual.siguiente
        k+=1
      if k==pos:
        anterior.siguiente=actual.siguiente
  #Dado un valor, determine cuántas veces está en la lista.
  def contar_ocurrencias(self, valor):
      actual = self.cabeza
      contador = 0
        
      while actual is not None:
          if actual.dato == valor:
              contador += 1
          actual = actual.siguiente
            
      return contador
 
  


       
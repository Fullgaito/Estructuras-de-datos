def papaCaliente(listaNom, num):
  simCola = Queue()
  for nom in listaNom:
    simCola.enqueue(nom)
  while simCola.size() > 1:
    for i in range(num):
 #     print('Num:', i)
      simCola.enqueue(simCola.dequeue())
    print('Sale:',simCola.dequeue())

  return simCola.dequeue()

# Programa principal
lista=['Miguel', 'Brigith','Byron', 'Espitia', 'Gumersindo', 'Dolores', 'Meylin']
print(lista)
print('Ganador: ',papaCaliente(lista, 7))
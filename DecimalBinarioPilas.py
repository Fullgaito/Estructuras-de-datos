def dec2bin(num):
  b = Stack()
  coc = abs(num)
  while coc > 0:
    res = coc % 2
    b.push(res)
    coc = coc // 2
  cad = ''
  while not b.isEmpty():
    cad = cad + str(b.pop())
  if num < 0:
    cad = '-' + cad
  return cad
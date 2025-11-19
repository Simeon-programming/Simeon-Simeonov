matrix = [                        ###[
    [1, 4, 13, 6],
    [8, 2, 9, 3],
    [10, 11, 5, 7],
    [13, 4, 6, 8],
    [1, 2, 3, 4]
]
suma = 0
stop =False
for row in matrix:
    for element in row:
      if element == 13:
        continue
      elif element == 7:
        break
      else:
         suma += element
    if stop:
        break
print("Suma na elementite e: ", suma)    
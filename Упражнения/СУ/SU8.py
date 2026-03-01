start = int(input("Vuvedete nachana stojnost: "))
kraj = int(input("Vuvedete krajna stojnost: "))

if start % 2 == 1:
    print("Purvoto nechetno chislo v intervala", start, kraj," e", start )
else:
    print("Purvoto nechetno chislo v intervala ", [start, kraj], "e", start+1)
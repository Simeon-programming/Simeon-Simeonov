chislo = int(input("Vuvedete chislo: "))
result = []
for i in range(1, chislo+1):
    if chislo % i == 0:
        result.append(i)
print(result)
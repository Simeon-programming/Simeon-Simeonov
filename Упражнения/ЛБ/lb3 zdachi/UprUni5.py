def delene (n):
    result = []
    for i in range(1, n+1):
        if i % 3 == 0 :
            result.append(i)
        elif i % 3 != 0:
            print("You didn't enter only whole numbers!")
    return result

chis = int(input("Enter a whole number: "))
kratni = delene(chis)
print("The numbers from 1 to ",chis, "that cn be devided by 3 are", kratni )

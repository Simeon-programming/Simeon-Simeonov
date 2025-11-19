def suma_na_deliteli(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
            print(i)
    return suma

number = int(input("Въведете цяло число: "))
result = suma_na_deliteli(number)
print("Сумата на делителите на", number, "е", result)

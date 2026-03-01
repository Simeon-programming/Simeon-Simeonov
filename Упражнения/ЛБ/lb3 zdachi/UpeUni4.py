#Напишете програма, която въвежда цяло число n и извежда сумата на всички негови делители. Решението трябва да използва функция и for цикъл.
def func(n):
    suma = 0
    for i in range(1, n + 1):
        if i % n == 0:
            suma += i
            print("Сумата е: ")
    return suma
number = int(input("Въведете число: "))
result = func(number)
print("Сумата на делителите на", number, "е", result)
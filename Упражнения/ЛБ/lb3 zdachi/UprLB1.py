#Напишете програма, в която потребителят въвежда цяло число. Програмата трябва да създаде два списъка – първият да съдържа четните цифри на числото, а вторият – нечетните цифри.
def func(num):
    list1 = []
    list2 = []
    for i in str(num):
        digit = int(i)
        if digit % 2 == 0:
            list1.append(digit)
        else:
            list2.append(digit)
    return list1, list2


number = input("Въведете цяло число: ")
try:
    chetni, nechetni = func(number)
    print("Това са числата, които се делят на две:", chetni)
    print("Това са числата, които не се делят на две:", nechetni)
except ValueError:
    print("Въведете само числа!")





        


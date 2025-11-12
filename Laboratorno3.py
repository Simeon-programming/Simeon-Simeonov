def ocenki (broi):
    obshto = 0
    slab = 0
    otlichni = 0

    for i in range(broi):
        grade = float(input(f"Въведи оценка на ученик {i + 1}: "))
        obshto += grade

        if grade < 3:
            slab += 1
        elif grade == 6:
            otlichni += 1

    average = obshto / broi
    print("\nСреден успех:", round(average, 2))
    print("Брой слаби оценки:", slab)
    print("Брой отлични оценки:", otlichni)

n = int(input("Колко ученици има в класа? "))
ocenki(n)

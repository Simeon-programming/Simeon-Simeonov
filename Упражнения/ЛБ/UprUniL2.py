total = 0
while True:
    chisla = input("Vuvedete chisla: ")
    try:
        number = float(chisla)
        total += number
    except ValueError:
        print("Vie vuvedohte chislo!")
        break
print("Sumata na chislata e:", total)

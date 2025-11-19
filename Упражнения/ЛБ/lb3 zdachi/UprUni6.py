def nai_golqmo (n):
    max = n[0]
    for i in n:
        if i > max:
            max = i
    return max


text = input("Въведете числа с интервали: ")
chisla = [int(x) for x in text.split()]
result = nai_golqmo(chisla)
print("Най-голямото число е:", result)
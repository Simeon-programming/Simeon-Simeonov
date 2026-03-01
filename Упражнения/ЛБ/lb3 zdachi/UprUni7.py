def po_golemi (numbers):
    average = sum(numbers)/len(numbers)
    result = []
    for num in numbers:
        if num > average:
            result.append(num)
    return result, average

text = input("Vuvedete chislata razdeleni s interval:")
chisla = [int(x) for x in text.split()]
greater, avg = po_golemi(chisla)
print("Srednata stoinost e : ", avg)
print("Chislata po-golemi ot srednoaritmetichnoto sa: ", greater)
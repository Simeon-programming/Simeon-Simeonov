#Напишете програма, в която потребителят въвежда текст. Програмата трябва да изведе броя на думите и броя на различните думи в текста
def func (text):
    words = text.split()
    obshto_dumi = len(words)
    razlichni = len(set(words))
    return obshto_dumi, razlichni
 
n = input("Въведете текст: ")
obshto_dumi, razlichni = func(n)
print("Брой на всички думи: ", obshto_dumi)
print("Брой на различни думи: ", razlichni)
    
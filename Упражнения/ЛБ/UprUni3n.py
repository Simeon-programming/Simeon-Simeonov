def pozdrav():
    chislo = input("Enter a number: ")
    if chislo.isdigit() > 0:
        chislo = int(chislo)
        for i in range(chislo):
            print("Hello Python")
    elif int(chislo) == 0:
        print("Enter a number greater than 0!")  
    elif int(chislo) < 0:
        print("Enter a positive number!")
    else:
        print("You entered a word.")
       

pozdrav()
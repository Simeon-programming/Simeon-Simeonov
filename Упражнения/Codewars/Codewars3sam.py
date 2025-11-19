def otr_chislo():
    s = input("Enter a number: ")
    try:
        num = float(s)
        if num < 0:
           print(num)
        else:
            print(-num)
        print("This is the negative number: ")
    except ValueError:
        print("Try again!")

otr_chislo()
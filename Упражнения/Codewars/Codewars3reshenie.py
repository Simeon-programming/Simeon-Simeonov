def chislo():
    s = input("Enter a number: ")

    try:
        num = float(s)  # Convert input to float (works for both int and decimal)
        if num < 0:
            print(num)
        else:
            print(-num)
        print("This is your number.")
    except ValueError:
        print("You entered a word. Try again!")

chislo()

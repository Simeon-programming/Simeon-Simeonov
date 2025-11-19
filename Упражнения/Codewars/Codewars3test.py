def chislo():
    s = input("Enter a number: ")

    # Check if the input is a valid number (including negative and decimal)
    if s.replace('.', '', 1).isdigit() or (s.startswith('-') and s[1:].replace('.', '', 1).isdigit()):
        num = float(s)

        if num > 0:
            print(-num)
        elif num < 0:
            print(num)
        else:
            print(0.0)

        print("This is your number.")
    else:
        print("You entered a word. Try again!")

chislo()

def chislo():
    num = input("Enter a number: ")
    if num.replace('.', '', 1).isdigit() or (num.startswith('-') and num[1:].replace('.', '', 1).isdigit()):
        s=float(num)
        if s > 0:
                print(-s)
        else:
                print(s)
    else:
        print("You didn't enter a number! Try again!")




chislo()


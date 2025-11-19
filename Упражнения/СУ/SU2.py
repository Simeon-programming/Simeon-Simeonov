ocenka = int(input("Vuvedete tochkite: "))
if ocenka > 100:
    print("Ne mojete da vuvedete chislo po-golqmo ot 100")
elif ocenka >= 90:
    print("6")
elif ocenka >= 80:
    print("5")
elif ocenka >= 70:
    print("4")
elif ocenka >= 60:
    print("3")
else:
     print("2")
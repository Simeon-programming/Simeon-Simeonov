def func ():
    vuvedi = input("Vuvedi duma: ")
    rechnik = {
        "glavni" : '0', 
        "malki" : '0',
        "drugi" : '0'
    }
    golemi = 0
    drebni = 0
    razlichni = 0
    for i in vuvedi:
        if i.isupper():
            golemi += 1
            rechnik["glavni"] = golemi
        elif i.islower():
            drebni += 1
            rechnik["malki"] = drebni
        else:
            razlichni += 1
            rechnik["drugi"] = razlichni
    print(rechnik)
func()
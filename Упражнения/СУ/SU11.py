import random 
kamuk = "kamuk"
nojici = "nojici"
hartiq = "hartiq"
wins = {
    "kamuk": "nojici",
    "nojici": "hartiq",
    "hartiq": "kamuk"
}
izbor = input("Izberete (kamuk, nojica ili hartiq): ")
options = [kamuk, nojici, hartiq]

    
computer_izbor = random.choice(options)
print("Komputura izbra:", computer_izbor)
if izbor == computer_izbor:
    print("Ravenstvo!")
elif wins[izbor] < computer_izbor:
    print("Vie gubite")
else:
    print("Vie pechelite")

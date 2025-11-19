def hello() :
    print("Hello!")

hello()
hello()
###
def zdr(name) :
    print("Zdravej " + name)

zdr("gotin")
zdr("manqk")
#trqbva da ima "str" na godinite ma ne znam zashto haha
def dvete(imence, godinki):
    print("Zdravej " + imence + "! Ti si na " + str(godinki) + "!")

dvete("Moni", 9)
###
def proba(godini = input("Na kolko si godini: "), imeto = input("Kakvo e imeto ti? ")):
    print(f"Zdravej  {imeto} ! Ti si na {godini} godini!")
    print("Zdravej " + imeto + "! Ti si na " + godini + " godini!")


proba()
####
def neshto(znaesh):
    print(f"Zdravej {znaesh}!")
    return znaesh,  "Simo", 10
print(neshto("Krasen"))

###
age = 8
def test():
    print(age)

print(age)
test()

# na 2 chasa i 23 ima oshte malko za funkcii
#if Ako na condition sloja "True", to togava shte stigne do purviq red i nqma da chete natatuk, no ako e "False" shte chete dokato nameri takova kakvoto da otgovarq, kato ako nqma takova kakvoto da otgovarq shte izvede "else"
condition = True
name = input("Vuvedete ime: ")

if condition == True:
    print("The condition was true")
elif name == "Roger":
    print("Hi Roger")  
if name == "Joe":
    print("Hello Joe")
else:
    print("The conditions are not fullfilled")
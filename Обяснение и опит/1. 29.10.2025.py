#izvejdane na age kato purvoto se vdiga na stepeta na vtoroto choslo
age = 8
age **= 2
print (age) 

#sushtoto obache sus subirane
age = 8
age += 2
print (age) 

#izvejdane na promenliva, izvejdane na tochno opredelena bukva, izvejdane na chast ot dumata (bukvata na poslednoto chislo ne se vkluchva)
name = "Moni e mnogo gotin"
print(name)
print(name[2])
print(name[1:6])

#booleans
done = False
if done:
    print("yes")
else:
    print("no")    
#ako e 0 daa False, ako e drugo chislo dava True, i ako e string i e prazen sushto shte dade False, a ako e s duma True
done = -1
if done:
    print("yes")
else:
    print("no") 

done = "dgd"
if done:
    print("yes")
else:
    print("no")     


#absolutna stoinost , zakruglqne, zkuglqne do znaka sled zapetaikata
print(abs(-5.5))  
print(round(9.6))
print(round(6.255254, 2))

#input
vuzrast = input("Na kolko godini ste: ")
print("Tvoqta vuzrast e " + vuzrast)
geschikt = True


#naam
naam = input("|Wat is uw naam: ")


#de leeftijd
leeftijd = int(input("|Wat is uw leeftijd?: "))
if leeftijd >= 21:
    print("|U bent oud genoeg.")
else:
    print("|U bent te jong.")
    geschikt = False


#lust banaan
banaan = input("|Lust u een banaan? Y/N: ").lower()
if banaan == "y":
    print("|Nice")
else:
    print("|Why?")
    geschikt = False


#wat is 9 + 10
wiskunde = input("|Wat is 9 + 10?: ")
if wiskunde == "21":
    print("|Je IQ is hoog genoeg.")
else:
    print("|Small brain.")
    geschikt = False


#IMPOSTER?
vent = input("|Heb je gevent? Y/N: ").lower()
if vent == "n":
    print("|Red sus.")
else:
    print("|You sus.")
    geschikt = False


#Ervaringen 
ervaring = input("|Heeft u ervaring in een van de volgende dieren-dressuur/jongleren/acrobatiek?: ").lower()
if ervaring == "dieren-dressuur":
    jaar = input("|Hoeveel jaar ervering heeft u hier in?: ")
    if jaar >= 4:
        print("Je hebt genoeg ervaring.")
    else:
        print("Je hebt niet genoeg ervaring")
        geschikt = False
if ervaring == "jongleren":
    jaar = input("|Hoeveel jaar ervering heeft u hier in?: ")
    if jaar >= 5:
        print("Je hebt genoeg ervaring.")
    else:
        print("Je hebt niet genoeg ervaring")
        geschikt = False
if ervaring == "acrobatiek":
    jaar = input("|Hoeveel jaar ervering heeft u hier in?: ")
    if jaar >= 3:
        print("Je hebt genoeg ervaring.")
    else:
        print("Je hebt niet genoeg ervaring")
        geschikt = False
else:
    print("|Je moet eerst ergens ervaring in hebben.")
    geschikt = False


#Diploma MBO-4 Ondernemen
diploma = input("|Bent u in bezit van een diploma MBO-4 Ondernemen? Y/N: ").lower()
if diploma == "y":
    print("|U bent geschikt.")
else:
    print("|U bent niet geschikt.")


#Heeft persoon rijbewijs
rijbewijs = input("|Heeft u een geldig vrachtwagen rijbewijs? Y/N: ").lower()
if rijbewijs == "y":
    print("|Je voldoet aan deze voorwaarde.")
else:
    print("|Je moet eerst een vrachtwagen rijbewijs halen.")
    geschikt = False


#Hoge hoed
hoed = input("|Bent u in bezit van een hoge hoed? Y/N: ").lower()
if hoed == "y":
    print("|Heel goed.")
else:
    print("|Zonder hoge hoed ben je niet geschikt.")
    geschikt = False


#Man of vrouw?
gember = input("|Bent u een man of vrouw?: ").lower()
if gember == "man":
    snor = input("|Hoe breed is uw snor in cm?: ")
    if int(snor) > 10:
        print("|U bent geschikt.")
    else:
        print("|U bent niet geschikt.")
        geschikt = False
elif gember == "vrouw":
    haar = input("|Hoe lang is uw rood krulhaar in cm?: ")
    if int(haar) >= 20:
        print("|U bent geschikt.")
    else:
        print("|U bent niet geschikt.")
        geschikt = False
else:
    print("|U bent niet geschikt.")
    geschikt = False


#Lengte
lengte = int(input("|Hoe lang bent u in cm?: "))
if lengte >= 150:
    print("|Je bent lang genoeg.")
else:
    print("|Je bent te klein.")
    geschikt = False


#gewicht
gewicht = int(input("|Wat is uw gewicht?: "))
if gewicht > 90:
    print("|U bent geschikt.")
else:
    print("|U bent niet geschikt.")
    geschikt = False


#Certificaat
papiertje = input("Heeft U het Certificaat “Overleven met gevaarlijk personeel”? Y/N: ").lower()
if papiertje == "y":
    print("|U bent geschikt.")
else:
    print("|U bent niet geschikt.")
    geschikt = False


#resultaat
if geschikt == True:
    print("|U bent geschikt om een vervolg gesprek te doen.")
if geschikt == False:
    print("|U bent niet geschikt voor deze baan.")

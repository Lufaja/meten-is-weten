#uitleg
print("------------------------------------------------------------------")
print("Beantwoord de vragen met ja of nee.")
print(" ")

#vragen over de kaas
geel = input("Is de kaas geel?               :").lower()
if geel == "ja":
    gaten = input("Zitten er gaten in?            :").lower()
    if gaten == "ja":
        duur = input("Is de kaas belachelijk duur?   :").lower()
        if duur == "ja":
            print("De kaas is een Emmenthaler.")
        else:
            print("De kaas is een Leerdammer.")
    else:
        steen = input("Is de kaas hard als steen?     :").lower()
        if steen == "ja":
            print("De kaas is een Pamigiano Reggiano.")
        else:
            print("De kaas is een Goudse kaas.")
else:
    schimmel = input("Heeft de kaas blauwe schimmels?:").lower()
    if schimmel == "ja":
        korst = input("Heeft de kaas een korst?       :").lower()
        if korst == "ja":
            print("De kaas is een Bleu de Rochbaron.")
        else:
            print("De kaas is een Foume d'Ambert.")
    else:
        korst = input("Heeft de kaas een korst?       :").lower()
        if korst == "ja":
            print("De kaas is een Camembert.")
        else:
            print("De kaas is een Mozzerela.")
print("------------------------------------------------------------------") 
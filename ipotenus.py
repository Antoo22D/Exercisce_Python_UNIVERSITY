# Calcolare l'ipotenusa di un triangolo rettangolo con i due cateti forniti in # input. Ripetere il calcolo quante volte si vuole.
import math
print("Teorema di Pitagora") continui = "S"
while (continui != "N" and continui != "n"):
    cateto1 = float(input("Cateto 1 : "))
    cateto2 = float(input ("Cateto 2 : "))
    ipotenusa = math.sqrt(math.pow(2, cateto1) + math.pow(cateto2, 2))
    ipotenusa = round(ipotenusa, 2)
# oppure: ipotenusa=((int)(ipotenusa*100))/100
print("Ipotenusa del rettangolo = " + str(ipotenusa))
continui = str(input("Altri calcoli ? "))
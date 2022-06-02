n=int(input("Voto conseguito: "))
if n<0 or n>30:
    print("voto non valido")
elif n>=18:
    print("esame superato")
else:
    print("Bocciato")
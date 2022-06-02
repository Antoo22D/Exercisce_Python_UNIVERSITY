frase=input()
vocali=["a","e","i","o","u"]
risultato=""
prima=""
seconda=""

for i in range(len(frase)):
    if frase[i] in vocali:
        risultato+=frase[i]+"f"+frase[i]
    else:
        risultato+=frase[i]
for j in range(len(risultato)//2):
    prima+=risultato[j]
for z in range(len(risultato)//2,len(risultato)):
    seconda+=risultato[z]
print(seconda+prima)


def pari_DISP(alfabeto,miaseq,n1,n2):
  if len(miaseq)==0:
    print("",end="")
  output=[]
  
  for carattere in range(len(alfabeto)):
    if carattere+1%2==0:
      return output

def main():
  alfabeto=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  n1=int(input("Inserisci n1: "))
  n2=int(input("Inserisci n2: "))
  seq=input("Scrivi qui la parola da cifrare: ")
  miaseq=[]
  while seq!=".":
    miaseq.append(seq)
    seq=input("Scrivi qui la parola da cifrare: ")
  cifra=pari_DISP(alfabeto, miaseq, n1, n2)
  print(cifra,end="")
main()
#----------------------------------------------------------#

''' Pseudo codice by Simone


def encrypt(sequence, n1, n2):
  # Se la sequenza è vuota restituisci la stringa vuota
  if len(sequence) == 0:
    return ''

  output = []

  # per ogni carattere della sequenza di input

    # IF l'indice corrispondente al carattere della sequenza di input è PARI:

      # spostati a SINISTRA di n2 posizioni nell'alfabeto partendo dalla posizione
      # corrispondente al carattere della sequenza di input. Appendi il nuovo carattere
      # all'array "output"

    # ELSE:

      # spostati a DESTRA di n1 posizioni nell'alfabeto partendo dalla posizione
      # corrispondente al carattere della sequenza di input. Appendi il nuovo carattere
      # all'array "output"      


  # trasforma l'array di caratteri "output" in una stringa e la restituisce
  return ''.join(output)

'''













'''
const alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

function getIndex(character) {
  return 0;
}

//
function encryptPari(n, character) {
  const index = getIndex(character);
  
}

function encryptDispari(n, character) {
  return 'x';
}

function encrypt(input, n1, n2) {
  const inputArray = input.split('');
  const output = [];

  if (inputArray.length === 0) {
    return '';
  }

  // for each element of the array
  for (let i = 0; i < inputArray.length; i++) {
    // pari
    if ((i + 1) % 2 === 0) {
      output.append(encryptPari(n2, inputArray[i])) // va indietro
    } else { // dispari
      output.append(encryptDispari(n1, inputArray[i])) // va avanti
    }
  }

  return output.join('');
}

const n1 = 2
const n2 = 4
const input = 'sedia'
const output = encrypt(input, n1, n2);
console.log(output);


// 5
// s e d i a

// u a f e c
'''
'''.'''












'''
def converti (alfabeto,miaseq,n1,n2):
if len(miaseq)==0:
        print("Vuota")
    else:
        for i in range(len(miaseq)):
            dispari.append()
            for j in range(len(miaseq)):
                pari.append(len(miaseq)//2==0)
                for i in dispari:
                    if i==len(miaseq)-1:
                        miaseq[i]+=alfabeto[0]
                    else:
                         occc
                for j in pari:
                    if j==len(miaseq)-1:
                        miaseq[j]+=alfabeto[0]        
    return miaseq 
'''
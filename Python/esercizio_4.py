#slicing
stringa = "Classe quarta A Robotica"
print(f"Il primo carattere della stringa è: {stringa[0]}")
print(f"L'ultimo carattere della stringa è: {stringa[-1]}")

#stringa[15] = "B"
#le stringhe sono immutabili
#TypeError: 'str' object does not support item assignment

stringaNuova = stringa[0:14] + "B" +stringa[15:]
print(f"La nuova stringa è: {stringaNuova}" )

# prende i caratteri a partire da quello con indice 0 
#fino a quello con indice 6 escluso
"""print(stringa[0:6])

print(stringa[6:])

print(stringa[:-2])

print(stringa[ : :-1])"""
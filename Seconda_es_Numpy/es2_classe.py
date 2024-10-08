# 1. Creazione dell'array
# Definisci una funzione che crea un array NumPy di due dimensioni (30 * 24) che riporta le temperature orarie del mese di Settembre.
# Inizializza i valori con numeri decimali casuali compresi tra 10 e 30 gradi Celsius (tip: usa np.random.uniform()).
# Note: for reproducibility, set seed at the beginning of the function definition using np.random.seed(100)

# 2. Temperatura più alta e più bassa
# Trova i valori di temperatura più alta e più bassa

# 3. Temperatura media giornaliera
# Per ogni giorno (quindi per ogni riga), calcola la temperatura media e crea un nuovo array di 30 elementi che rappresenta la temperatura media giornaliera.
# Trova i giorni con la temperatura media più alta e la temperatura media più bassa.

# 4. Aumento di temperatura
# Sono stati rilevati alcuni problemi nella calibrazione del misuratore, è necessario aumentare di 2 gradi ogni temperatura rispetto a quanto misurato.

# 5. Modifica di alcuni valori
# Modifica i valori dell'array in modo che il valore massimo possibile sia 30.

# 6. Quante volte sono stati registrati più di 23 gradi?
# Conta il numero di volte in cui la temperatura registrata è stata superiore a 23 gradi.

#7. Confronto di valori medi
#Calcola la differenza tra la temperatura media dei primi 3 giorni di Settembre e quella degli ultimi 3 giorni.

import numpy as np

def creaArray():
  np.random.seed(100)
  return np.random.uniform(10,30,[30,24])

array=creaArray()
array

array.max()
array.min()

media=array.mean(axis=1)
media.shape

media.argmin()
media.argmax()

array + 2

#5
np.where(array>30, 30, array)

#6
bools = array > 23
bools.sum()

#before=media[0:4]
#after=media[26:]
#before-after

#creazione di una nuova colonna
mediana=np.median(array, axis=1)
mediana
mediana.reshape(30,1)
np.concatenate((array, mediana.reshape(30,1)), axis=1)
np.hstack((array, mediana.reshape(30,1))) #stessa cosa di prima, produce lo stesso output


#7
before = array[:3]
b_mean = before.mean()
after = array[-3:]
a_mean = after.mean()
b_mean - a_mean
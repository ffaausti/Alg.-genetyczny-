import numpy as np 
import random 


def mutacja(array):
    probability = random.random()
    print(probability)
    if probability < 0.1:
        miejsce_zajscia = random.randint(0, array.shape[0]-1) #ma wybierać miejsce zajscia mutacji
        print("Miejsce zajscia mutacji:", miejsce_zajscia +1) #te + i - są kosmetyczne, do sprawdzenia czy indeksy się zgadzają
        array[miejsce_zajscia] = 1 - array[miejsce_zajscia]
    return array

lista = np.array([1, 0, 1, 1, 0, 1, 1, 0])

print(lista)

print(mutacja(lista))

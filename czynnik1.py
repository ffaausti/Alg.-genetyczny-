def zliczanie_wartosci_nonogramu(kolumny, wiersze):
    wartosci_kolumn_nonogramu = []
    wartosci_wierszy_nonogramu = []

    for i in range(len(kolumny)):
        wartosci_kolumn_nonogramu.append(sum(kolumny[i]))
    for i in range(len(wiersze)):
        wartosci_wierszy_nonogramu.append(sum(wiersze[i]))
    return wartosci_wierszy_nonogramu, wartosci_kolumn_nonogramu

def zliczanie_wartosci_osobnika(osobnik_matryca):
    wartosci_wierszy_osobnika = []
    wartosci_kolumn_osobnika = []
    for i in range(5):
        count = np.count_nonzero(osobnik_matryca[0:,i] == 1)
        wartosci_kolumn_osobnika.append(count)
    for i in range(5):
        count = np.count_nonzero(osobnik_matryca[i,0:] == 1)
        wartosci_wierszy_osobnika.append(count)
    return wartosci_wierszy_osobnika, wartosci_kolumn_osobnika

def porownywanie_wartosci_1(wartosci_kolumn_nonogramu,wartosci_wierszy_nonogramu, wartosci_kolumn_osobnika, wartosci_wierszy_osobnika):
    lista_bledow = []
    for i in range(len(kolumny)):
        blad = abs(wartosci_kolumn_nonogramu[i]-wartosci_kolumn_osobnika[i])
        blad2 = abs(wartosci_wierszy_nonogramu[i]-wartosci_wierszy_osobnika[i])
        lista_bledow.append(blad)
        lista_bledow.append(blad2)
        
    return sum(lista_bledow)

wartosci_wierszy_osobnika, wartosci_kolumn_osobnika = zliczanie_wartosci_osobnika(osobnik_matryca)   
wartosci_wierszy_nonogramu, wartosci_kolumn_nonogramu = zliczanie_wartosci_nonogramu(kolumny, wiersze)
print(porownywanie_wartosci_1(wartosci_kolumn_nonogramu, wartosci_wierszy_nonogramu, wartosci_kolumn_osobnika, wartosci_wierszy_osobnika))

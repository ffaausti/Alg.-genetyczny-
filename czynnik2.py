def zliczanie_przerw_nonogram(kolumny, wiersze):
    lista_przerw_kolumn_nono = []
    lista_przerw_wierszy_nono = []
    lista_przerw_kolumn_nono.append([len(i) for i in kolumny])
    lista_przerw_wierszy_nono.append([len(i) for i in wiersze])
    return lista_przerw_kolumn_nono[0], lista_przerw_wierszy_nono[0]


def zliczanie_przerw_osobnik(kolumny, wiersze, osobnik_matryca):
    
    lista_przerw_kolumn_os = []
    lista_przerw_wierszy_os = []
    for column in osobnik_matryca.T: #dla kolumn
        uciete1 = [column[0]]  
        for i, c in enumerate(column[1:]):
            if c != column[i]:
                uciete1.append(c)
        lista_przerw_kolumn_os.append(uciete1.count(0))

    for verse in osobnik_matryca:  #dla wersów
        uciete = [verse[0]]  
        for y, d in enumerate(verse[1:]):
            if d != verse[y]:
                uciete.append(d)
        lista_przerw_wierszy_os.append(uciete.count(0))
        
    return  lista_przerw_kolumn_os, lista_przerw_wierszy_os

def porownywanie_wartosci_0(lista_przerw_kolumn_nono, lista_przerw_wierszy_nono,lista_przerw_kolumn_os, lista_przerw_wierszy_os ):
    lista_bledow_0 = []
    for i in range(len(kolumny)):
        blad = abs(lista_przerw_kolumn_nono[i]-lista_przerw_kolumn_os[i])
        blad2 = abs(lista_przerw_wierszy_nono[i]-lista_przerw_wierszy_os[i])
        lista_bledow_0.append(blad)
        lista_bledow_0.append(blad2)
    return sum(lista_bledow_0)

lista_przerw_kolumn_nono, lista_przerw_wierszy_nono = zliczanie_przerw_nonogram(kolumny, wiersze)
lista_przerw_kolumn_os, lista_przerw_wierszy_os = zliczanie_przerw_osobnik(kolumny, wiersze, osobnik_matryca)
print(porownywanie_wartosci_0(lista_przerw_kolumn_nono, lista_przerw_wierszy_nono, lista_przerw_kolumn_os, lista_przerw_wierszy_os))

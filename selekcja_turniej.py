#lista_osobników = lista arrayów 01 lub lista przypisanych im indeksów, lista_f_przystosowania = lista odpowiadającejmu arrayowi błędu
def turniej(lista_osobnikow, lista_f_przystosowania): 
    slownik = {lista_osobnikow[i]: lista_f_przystosowania[i] for i in range(len(lista_osobnikow))}
    nowa_populacja = []
    for i in range(len(lista_osobnikow)):
        lista_turniejowa = []
        for i in range(5):
            lista_turniejowa.append(random.choice(lista_f_przystosowania))
            winner = min(lista_turniejowa)
        nowa_populacja.append({i for i in slownik if slownik[i]==winner})
    return nowa_populacja

def generowanie_populacji(liczba_osobnikow, liczba_genow):
    pierwsza_populacja = []
    for i in range(liczba_osobnikow):
        osobnik = np.random.rand(1, liczba_genow).round()
        pierwsza_populacja.append(osobnik)
    return pierwsza_populacja

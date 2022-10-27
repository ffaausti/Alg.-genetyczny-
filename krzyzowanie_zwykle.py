def krzyzowanie(osobnik1, osobnik2, liczba_genow): #osobnik =array
    miejsce_krzyzowania = random.randint(1,liczba_genow)
    print("Miejsce krzyżowania:", miejsce_krzyzowania)
    dziecko1 = np.concatenate(np.split(osobnik1[:miejsce_krzyzowania], 1) + np.split(osobnik2[miejsce_krzyzowania:], 1))
    dziecko2 = np.concatenate(np.split(osobnik2[:miejsce_krzyzowania], 1) + np.split(osobnik1[miejsce_krzyzowania:], 1))
    return dziecko1, dziecko2

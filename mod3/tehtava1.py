
kuhan_pituus = input("Anna kuhan pituus: ")
int_kuhan_pituus = int(kuhan_pituus)
puuttuva_pituus = 37 - int_kuhan_pituus
puuttuvan_pituuden_ilmoitus = str(puuttuva_pituus) + "cm liian pieni "

if int_kuhan_pituus < 37:
    print("Laske kala takaisin järveen")
    print(puuttuvan_pituuden_ilmoitus)
else:
    print("Kala on tarpeeksi suuri")
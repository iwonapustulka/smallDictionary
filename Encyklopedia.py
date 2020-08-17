from copy import copy

tab = dict()
with open('Noble', 'r', encoding="utf-8") as f:
    temp = dict()
    nazwa = ""
    for line in f:
        value = line.split()
        if value[0] == "Osoba":
            if tab is dict():
                tab[nazwa] = temp
            zm = ""
            for val in range(1, len(value)):
                zm = zm + value[val] + (" " if val != len(value) - 1 else "")
            nazwa = zm
        if value[0] == "Rok":
            zm2 = ""
            for val in range(1, len(value)):
                zm2 = zm2 + value[val] + (" " if val != len(value) - 1 else "")
            temp["Rok"] = zm2
        if value[0] == "Kategoria":
            zm3 = ""
            for val in range(1, len(value)):
                zm3 = zm3 + value[val]
            temp["Kategoria"] = zm3 + (" " if val != len(value) - 1 else "")
            tab[nazwa] = copy(temp)

for id, key in enumerate(tab.keys()):
    print(str(id + 1) + ": " + key)

a = input("Podaj nazwisko noblisty ktorego chcesz poznac szczegoly: ")

for key, result in tab.items():
    if a in key.lower():
        print(key, ": ", result)
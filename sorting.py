import random

# ÚKOL: Selection Sort - implementace
def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(seznam_c):

    kopie_c = seznam_c.copy()
    delk = len(kopie_c)

    for i in range(delk):
        for j in range(i+1, delk):
            if kopie_c[j] < kopie_c[i]:
                x = kopie_c[i]
                kopie_c[i] = kopie_c[j]
                kopie_c[j] = x

    return kopie_c



# ÚKOL: Bubble Sort - implementace
def bubble_sort(seznam_c):

    kopie_cisel = seznam_c.copy()
    delka = len(kopie_cisel)

    for i in range(delka):
        for j in range(0, delka - i - 1):
            if kopie_cisel[j] > kopie_cisel[j+1]:
                x = kopie_cisel[j]
                kopie_cisel[j] = kopie_cisel[j+1]
                kopie_cisel[j + 1] = x

    return kopie_cisel



# Selection sort: „najdu nejmenší a dám ho dopředu“
# Bubble sort: „v ětší čísla posouvám doprava“



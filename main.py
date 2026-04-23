# ÚKOL: Selection Sort - implementace
from sorting import random_numbers
from sorting import selection_sort
from sorting import bubble_sort

def main():
    seznam = [5, 1, 4, 2, 8]
    print("Na začátku seznam:", seznam)
    print("Seřazený seznam:", selection_sort(seznam))


    nahodny_seznam = random_numbers(20)
    print("Na začátku náhodný seznam:", nahodny_seznam)
    print("Seřazené náhodný seznam:", selection_sort(nahodny_seznam))



# ÚKOL: Bubble Sort - implementace
    seznam = [5, 1, 4, 2, 8]
    print("Na začátku seznam:", seznam)
    print("Seřazený seznam:", bubble_sort(seznam))


    nahodny_seznam = random_numbers(20)
    print("Na začátku náhodný seznam:", nahodny_seznam)
    print("Seřazené náhodný seznam:", bubble_sort(nahodny_seznam))


if __name__ == "__main__":
    main()
from sorting import random_numbers
from sorting import selection_sort
from sorting import bubble_sort
from hodnoceni_studentu import StudentsGrades


# ÚKOL: Selection Sort - implementace
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



# ÚKOL: Udělení známky - metoda get_grade()
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print(results.get_grade(2))  # A (91 bodů)
    print(results.get_grade(6))  # A (100 bodů)
    print(results.get_grade(7))  # F (38 bodů)



# ÚKOL: Vyhledávání studentů s konkrétním počtem bodů - metoda find()
    print(results.find(100))  # [6]
    print(results.find(50))  # [4]
    print(results.find(77))  # []



# ÚKOL: Seřazení výsledků - metoda get_sorted()
    print(results.get_sorted())   # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    print(results.scores)         # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny




# ÚKOL: Demonstrace třídy
#1 už vypsaná výše
if __name__ == "__main__":
    main()
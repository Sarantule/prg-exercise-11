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
#2 Vypiš, kolik studentů psalo test (využij count()).
    celkem_s = results.count()
    print(f"Počet studentů: {celkem_s}")
#3 V cyklu vypiš pro každého studenta jeho pořadí (index), počet bodů a písmennou známku.
    for i, body in enumerate(results.scores):
        print(f"Student {i} {body} points – {results.get_grade(i)}")
#4 Najdi a vypiš indexy studentů, kteří měli plný počet bodů (100).
    plny = results.find(100)
    print(f"Studenti se 100 body: {plny}")
#5 Vypiš seřazené výsledky od nejhoršího po nejlepšího (pomocí get_sorted()).
    serazeno = results.get_sorted()
    print(serazeno)
#6 Vyzkoušej třídu i na náhodných datech. Importuj si random_numbers() ze sorting.py a vytvoř druhý objekt:
# zkopirovano jen
    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())



# 5.7 Bonusy
    print("Průměr skupinky:", results.average())
    print("Nejvyšší sk:", results.best())
    print("Nejnižší sk:", results.worst())
    print("Nedostali F:", results.pass_rate())
    print(results)  # použije str







if __name__ == "__main__":
    main()
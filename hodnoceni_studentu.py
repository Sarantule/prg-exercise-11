class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores
    def get_by_index(self, index):
        return self.scores[index]
    def count(self):
        return len(self.scores)


# ÚKOL: Udělení známky - metoda get_grade()
    def get_grade(self, index):
        pocet_b = self.scores[index]
        if pocet_b >= 90: # tabulka v zadani
            return "A"
        elif pocet_b >= 80:
            return "B"
        elif pocet_b >= 70:
            return "C"
        elif pocet_b >= 60:
            return "D"
        elif pocet_b >= 50:
            return "E"
        else:
            return "F"



# ÚKOL: Vyhledávání studentů s konkrétním počtem bodů - metoda find()
    def find(self, pocet_b):
        hled_indexy = []
        for i, cislo in enumerate(self.scores):
            if cislo == pocet_b:
                hled_indexy.append(i)
        return hled_indexy


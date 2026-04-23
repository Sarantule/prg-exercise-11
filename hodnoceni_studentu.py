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



# ÚKOL: Seřazení výsledků - metoda get_sorted()
    def get_sorted(self):

        kopie_cisel = self.scores.copy()
        delka = len(kopie_cisel)

        for i in range(delka):
            for j in range(0, delka - i - 1):
                if kopie_cisel[j] > kopie_cisel[j + 1]:
                    x = kopie_cisel[j]
                    kopie_cisel[j] = kopie_cisel[j + 1]
                    kopie_cisel[j + 1] = x

        return kopie_cisel



# 5.7 Bonusy (dobrovolné)
    #1
    def average(self):
        prumer = sum(self.scores)/len(self.scores)
        return prumer
    #2
    def best(self):
        nejvyssi = max(self.scores)
        return nejvyssi
    def worst(self):
        nejnizssi = min(self.scores)
        return nejnizssi
    #3
    def pass_rate(self):
        nedostaliF = 0
        for pocet_b in self.scores:
            if pocet_b >= 50:
                nedostaliF += 1
            pocet = nedostaliF/len(self.scores)
        return pocet
    #4
    def __str__(self):
        return f"StudentsGrades: {self.count()} studentů, průměr {self.average():.1f}"
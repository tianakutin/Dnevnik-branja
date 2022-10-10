class Knjiga:
    def __init__(self, naslov, avtor, ocena, mnenje, datum):
        self.naslov = naslov
        self.avtor = avtor
        self.ocena = ocena
        self.mnenje = mnenje
        self.datum = datum

knjige = []

class Stanje:
    def __init__(self, knjige):
        self.knjige = knjige
    
    def dodaj_knjigo(self, knjiga):
        self.knjige.append(knjiga)

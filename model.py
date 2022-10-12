import json

class Knjiga:
    def __init__(self, naslov, avtor, ocena, mnenje, datum):
        self.naslov = naslov
        self.avtor = avtor
        self.ocena = ocena
        self.mnenje = mnenje
        self.datum = datum

    def v_slovar(self):
        return {
            "naslov": self.naslov,
            "avtor": self.avtor,
            "ocena": self.ocena,
            "mnenje": self.mnenje,
            "datum": self.datum,
        }
    
    @staticmethod
    def iz_slovarja(slovar):
        return Knjiga(
            slovar["naslov"],
            slovar["avtor"],
            slovar["ocena"],
            slovar["mnenje"],
            slovar["datum"],
        )

class Stanje:
    def __init__(self, knjige):
        self.knjige = knjige
    
    def dodaj_knjigo(self, knjiga):
        self.knjige.append(knjiga)

    def shrani_v_datoteko(self, ime_datoteke):
        with open(ime_datoteke, 'w') as dat:
            slovar = self.v_slovar()
            json.dump(slovar, dat)
    
    def v_slovar(self):
        slovar = {}
        for i in range(len(self.knjige)):
            knjiga = self.knjige[i]
            slovar["knjiga{i}"] = knjiga.v_slovar()
        return slovar
    
    @staticmethod
    def preberi_iz_datoteke(ime_datoteke):
        with open(ime_datoteke) as dat:
            slovar = json.load(dat)
            return Stanje.iz_slovarja(slovar)

    @staticmethod
    def iz_slovarja(slovar):
        stanje = Stanje(
            [
                Knjiga.iz_slovarja(knjiga)
                for knjiga in slovar
            ]
        )
        return stanje
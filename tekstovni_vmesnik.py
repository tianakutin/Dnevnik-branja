from model import Knjiga, Stanje


DODAJ_KNJIGO = 'dodaj'
ZAKLJUCI = 'konec'


IME_DATOTEKE = "stanje.json"
try:
    stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    stanje = Stanje(knjige=[])



def tekstovni_vmesnik():
    print(pozdravno_sporocilo())
    while True:
        prikazi_osnovni_zaslon()
    
def pozdravno_sporocilo():
    return "Živjo"

def prikazi_osnovni_zaslon():
    izpisi_stanje()
    while True:
        ukaz = preberi_ukaz()
        if ukaz == DODAJ_KNJIGO:
            dodaj_knjigo()
            prikazi_osnovni_zaslon()
        elif ukaz == ZAKLJUCI:
            stanje.shrani_v_datoteko(IME_DATOTEKE)
            print('Nasvidenje!')
            break   


def preberi_ukaz():
    ukaz = input('Kaj želiš storiti? ')
    return ukaz

def dodaj_knjigo():
    naslov = input("Naslov knjige: ")
    avtor = input("Avtor knjige: ")
    ocena = input("Ocena knjige od 1 do 5: ")
    mnenje = input("Mnenje: ")
    datum = input("Datum, ko sem knjigo prebral: ")
    knjiga = Knjiga(naslov, avtor, ocena, mnenje, datum)
    stanje.dodaj_knjigo(knjiga)

def izpisi_stanje():
    for knjiga in stanje.knjige:
        print(f"""Naslov knjige: {knjiga.naslov}
        Avtor: {knjiga.avtor}
        Ocena: {knjiga.ocena}
        Mnenje: {knjiga.mnenje}
        Datum: {knjiga.datum}
        """)
    if not stanje.knjige:
        print(
            "Trenutno nimate še nobene knjige, zato morate eno najprej dodati."
        )


tekstovni_vmesnik()
from model import Knjiga, Stanje


DODAJ_KNJIGO = 'dodaj'
ZAKLJUCI = 'konec'

#IME_DATOTEKE = 'stanje.json'

#stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
stanje = ['knjiga1']

def tekstovni_vmesnik():
    print(pozdravno_sporocilo())
    while True:
        prikazi_osnovni_zaslon()
    
def pozdravno_sporocilo():
    return "Živjo"

def prikazi_osnovni_zaslon():
    print(prikazi_aktualno_prebrano())
    while True:
        ukaz = preberi_ukaz()
        if ukaz == DODAJ_KNJIGO:
            dodaj_knjigo()
            prikazi_osnovni_zaslon()
        elif ukaz == ZAKLJUCI:
            print("Nasvidenje!")
            break

def prikazi_aktualno_prebrano():
    return stanje

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
    stanje = stanje.append(knjiga.naslov)




tekstovni_vmesnik()
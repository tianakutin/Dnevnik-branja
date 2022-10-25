import bottle,time
from model import Knjiga, Stanje

DODAJ_KNJIGO = 'dodaj'
ZAKLJUCI = 'konec'


IME_DATOTEKE = "stanje.json"
try:
    stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    stanje = Stanje(knjige=[])


@bottle.get('/')
def osnovni_zaslon():
    return bottle.template('osnovni_zaslon.html', knjige = stanje.knjige)

@bottle.post('/dodaj_knjigo/')
def dodajanje_knjige():
    naslov = bottle.request.forms.getunicode('naslov')
    avtor = bottle.request.forms.getunicode('avtor')
    try:
        ocena = bottle.request.forms['ocena']
    except:
        ocena = ""
    mnenje = bottle.request.forms.getunicode('mnenje')
    datum = bottle.request.forms['datum']
    if naslov and avtor:
        for i in stanje.knjige:
            if i.naslov==naslov and i.avtor==avtor:
                return 'Vnesli ste že obstoječo knjigo.\n Pojdi nazaj '
                
        knjiga = Knjiga(naslov, avtor, ocena, mnenje, datum)
        stanje.dodaj_knjigo(knjiga)
        stanje.shrani_v_datoteko(IME_DATOTEKE)
        bottle.redirect('/')
    else:
        return 'Napisati morate naslov in avtorja.'

@bottle.post('/izbrisi_knjigo/')
def brisanje_knjige():
    knjiga = bottle.request.forms.getunicode('knjiga')
    stanje.izbrisi_knjigo(knjiga)

    stanje.shrani_v_datoteko(IME_DATOTEKE)
    bottle.redirect('/')

bottle.run(reloader=True, debug=True)
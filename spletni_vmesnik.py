import bottle
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
    return bottle.template('osnovni_zaslon.tpl', knjige = stanje.knjige)

@bottle.post('/dodaj_knjigo/')
def dodaj_opravilo():
    naslov = bottle.request.forms['naslov']
    avtor = bottle.request.forms['avtor']
    ocena = bottle.request.forms['ocena']
    mnenje = bottle.request.forms['mnenje']
    datum = bottle.request.forms['datum']
    if naslov and avtor:
        knjiga = Knjiga(naslov, avtor, ocena, mnenje, datum)
        stanje.dodaj_knjigo(knjiga)
        stanje.shrani_v_datoteko(IME_DATOTEKE)
        bottle.redirect('/')
    else:
        return 'NApisati morate naslov in avtorja.'

bottle.run(reloader=True, debug=True)
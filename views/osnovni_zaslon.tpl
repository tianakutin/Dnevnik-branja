% rebase('base.tpl')
<h1>Prebrane knjige</h1>
% if knjige != []:
%   for knjiga in knjige:
<hr>
<h2>Naslov knjige: {{knjiga.naslov}}</h2>
<p>Avtor: {{knjiga.avtor}}</p>
<p>Ocena: {{knjiga.ocena}}</p>
<p>Mnenje: {{knjiga.mnenje}}</p>
<p>Datum: {{knjiga.datum}}</p>
<hr>
%end

<form action="/dodaj_knjigo/" method="POST">
  Naslov: <input type="text" name="naslov">
  Avtor: <input type="text" name="avtor">
  Ocena: <input type="text" name="ocena">
  Mnenje: <input type="text" name="mnenje">
  Datum: <input type="text" name="datum">
  <button type="submit" value="bla" name="xy">Dodaj</button>
</form>

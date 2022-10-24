% rebase('base.tpl')
<h1>Knjige</h1>

<form action="/dodaj_knjigo/" method="POST">
  <label for="naslov">Naslov:</label><br>
  <input type="text" id="naslov" name="naslov"><br>
  <label for="avtor">Avtor:</label><br>
  <input type="text" id="avtor" name="avtor"><br><br>
  Ocena:
  %for i in range(1,6):
  <input type="radio" id="ocena" name="ocena" value="{{i}}">
  <label for="ocena">{{i}}</label>
  %end
  <br><br>
  <label for="mnenje">Mnenje:</label><br>
  <input type="text" id="mnenje" name="mnenje"><br><br>
  <label for="datum">Datum:</label>
  <input type="date" id="datum" name="datum">
  <input type="submit" value="Dodaj">
</form>

% if knjige != []:
%   for knjiga in knjige:
<hr>
<h2>Naslov knjige: {{knjiga.naslov}}</h2>
<p>Avtor: {{knjiga.avtor}}<br>
Ocena: {{knjiga.ocena}}<br>
Mnenje: {{knjiga.mnenje}}<br>
Datum: {{knjiga.datum}}</p>
<input type="button" onclick="alert('Hello World!')" value="Izbriši">
<hr>
%end


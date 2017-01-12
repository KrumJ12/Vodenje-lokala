% rebase('osnova.tpl')

<div class="container">

      <h4>Operacije</h4>
      <ul class="nav nav-pills nav-stacked">

        <li><a href="javascript:showhide('uniquename')">Dodaj zaposlenega</a></li>

      </ul><br>



<form method="post" id="uniquename" style="display:none;">
  <div class="form-group">
    <label for="ime">Ime</label>
    <input type="text" class="form-control" id="ime" name="ime" aria-describedby="emailHelp" placeholder="Vnesi ime zaposlenega">
  </div>

    <div class="form-group">
    <label for="priimek">Priimek</label>
    <input type="text" class="form-control" id="priimek" name="priimek" aria-describedby="emailHelp" placeholder="Vnesi priimek zaposlenega">
  </div>


    <div class="form-group">
    <label for="datum_rojstva">Datum rojstva</label>
    <input type="text" class="form-control" id="datum_rojstva" name="datum_rojstva" aria-describedby="emailHelp" placeholder="Vnesi datum rojstva oblike LLLL-MM-DD">
  </div>

  <div class="form-group">
    <label for="eposta">E-pošta</label>
    <input type="text" class="form-control" name = "eposta" id="eposta" aria-describedby="emailHelp" placeholder="Vnesi elektronski naslov">
  </div>

    <div class="form-group">
    <label for="funkcija">Funkcija</label>
    <select class="form-control" id="funkcija" name="funkcija">
      <option>Šef</option>
      <option>Vodja izmene</option>
      <option>Kuhar</option>
      <option>Natakar</option>
      <option>Ostalo osebje</option>
    </select>
  </div>


  <div class="form-group">
    <label for="telefon">Telefon</label>
    <input type="text" class="form-control" name = "telefon" id="telefon" aria-describedby="emailHelp" placeholder="Vnesi telefonsko številko oblike  040 400 800">
  </div>

  <div class="form-group">
    <label for="prebivalisce">Prebivališče</label>
    <input type="text" class="form-control" name = "prebivalisce" id="prebivalisce" aria-describedby="emailHelp" placeholder="Vnesi prebivališče">
  </div>

  <button type="submit" class="btn btn-primary">Potrdi</button>



</form>
</div>



<div class="container">

  <h2>Seznam zaposlenih:</h2> 
  <br>        
  <table class="table">

    <thead>
      <tr>
      
        <th>Ime</th>
        <th>Priimek</th>
        <th>Datum rojstva</th>
        <th>E-pošta</th>
        <th>Datum zaposlitve</th>
        <th>Telefon</th>
        <th>Prebivališče</th>
        <th>Uredi</th>
        <th>Odstrani</th>
      </tr>
    </thead>

    <tbody>

    % for zaposlen in seznam:
      <tr>

        <td>{{zaposlen['ime']}}</td>
        <td>{{zaposlen['priimek']}}</td>
        <td>{{zaposlen['datum_rojstva']}}</td>
        <td>{{zaposlen['e_posta']}}</td>
        <td>{{zaposlen['datum_zaposlitve']}}</td>
        <td>{{zaposlen['telefon']}}</td>
        <td>{{zaposlen['prebivalisce']}}</td>
        <td><a href="/zaposleni/{{zaposlen['id']}}/uredi">
                            <i class="glyphicon glyphicon-pencil"></i>
                        </a>
        </td>
        <td><a href="/zaposleni/{{zaposlen['id']}}/odstrani">
                            <i class="glyphicon glyphicon-trash"></i></a>
        </td>
      %end
      </tr>
    </tbody>
  </table>

  </div>

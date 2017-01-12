
% rebase('osnova.tpl')
<form method="post">

<div class="container">
  <h1>Želite odstraniti tega zaposlenega?</h2>
  <br>

  <h2>Podatki o zaposlenemu:</h2>  
   <br>       
  <table class="table table-bordered">
    <thead>
      <tr>
        <th>Ime</th>
        <th>Priimek</th>
        <th>Funkcija</th>
        <th>Datum rojstva</th>
        <th>E-pošta</th>
        <th>Datum zaposlitve</th>
        <th>Telefon</th>
        <th>Prebivališče</th>
      </tr>
    </thead>
    <tbody>

      <tr>
        <td>{{zaposlen['ime']}}</td>
        <td>{{zaposlen['priimek']}}</td>
        <td>{{zaposlen['datum_rojstva']}}</td>
        <td>{{zaposlen['funkcija']}}</td>
        <td>{{zaposlen['e_posta']}}</td>
        <td>{{zaposlen['datum_zaposlitve']}}</td>
        <td>{{zaposlen['telefon']}}</td>
        <td>{{zaposlen['prebivalisce']}}</td>
      </tr>

    </tbody>
  </table>


    <input value="{{zaposlen['id']}}" name="id_zap" type="hidden">
    <a href="/zaposleni" class="btn btn-primary">Pojdi nazaj</a>
    <button class="btn btn-danger" type="submit">Odstrani</button>
    
</form>

</div>
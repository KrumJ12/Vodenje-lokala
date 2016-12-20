% rebase('osnova.tpl')

<div class="container-fluid">
  <div class="row content">
    <div class="col-sm-3 sidenav">
      <h4>Operacije</h4>
      <ul class="nav nav-pills nav-stacked">

        <li><a href="#section2">Dodaj zaposlenega</a></li>

      </ul><br>

    </div>

    <div class="col-sm-9">



<div class="container">
  <h2>Seznam zaposlenih</h2>         
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

      %end
      </tr>
    </tbody>
  </table>
</div>

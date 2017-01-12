% rebase('osnova.tpl')

<div class="container-fluid">
  <div class="row content">
    <div class="col-sm-3 sidenav">
      <h4>Operacije</h4>
      <ul class="nav nav-pills nav-stacked">

        <li><a href="javascript:showhide('uniquename')">Dodaj dobavitelja</a></li>

      </ul><br>

    </div>

    <div class="col-sm-9">

 <form method="post" id="uniquename" style="display:none;">
  <div class="form-group">
    <label for="naziv">Naziv podjetja</label>
    <input type="text" class="form-control" id="ime" name="naziv" aria-describedby="emailHelp" placeholder="Vnesi naziv podjetja">
  </div>

    <div class="form-group">
    <label for="naslov">Naslov podjetja</label>
    <input type="text" class="form-control" id="priimek" name="naslov" aria-describedby="emailHelp" placeholder="Vnesi naslov podjetja">
  </div>


    <div class="form-group">
    <label for="telefon">Kontakt</label>
    <input type="text" class="form-control" id="datum_rojstva" name="telefon" aria-describedby="emailHelp" placeholder="Vnesi telefonsko številko">
  </div>

  <div class="form-group">
    <label for="eposta">E-pošta</label>
    <input type="text" class="form-control" name = "eposta" id="eposta" aria-describedby="emailHelp" placeholder="Vnesi elektronski naslov">
  </div>



  <div class="form-group">
    <label for="davcna_stevilka">Davčna številka</label>
    <input type="text" class="form-control" name = "davcna" id="davcna_stevilka" aria-describedby="emailHelp" placeholder="Davčna številka">
  </div>

  <div class="form-group">
    <label for="TRR">Transakcijski račun</label>
    <input type="text" class="form-control" name = "TRR" id="prebivalisce" aria-describedby="emailHelp" placeholder="Vnesi TRR">
  </div>

  <button type="submit" class="btn btn-primary">Potrdi</button>



</form>

<div class="container">
  <h2>Seznam dobaviteljev</h2>         
  <table class="table">

    <thead>
      <tr>
        <th>Naziv</th>
        <th>Naslov</th>
        <th>Telefon</th>
        <th>E-pošta</th>
        <th>Davčna številka</th>
        <th>TRR</th>
        <th>Uredi</th>
        <th>Odstrani</th>

      </tr>
    </thead>

    <tbody>

    % for dobavitelj in seznam:
      <tr>


        <td>{{dobavitelj['naziv']}}</td>
        <td>{{dobavitelj['naslov']}}</td>
        <td>{{dobavitelj['telefon']}}</td>
        <td>{{dobavitelj['e_posta']}}</td>
        <td>{{dobavitelj['davcna_stevilka']}}</td>
        <td>{{dobavitelj['trr']}}</td>
        <td><a href="/dobavitelji/{{dobavitelj['id']}}/uredi">
                            <i class="glyphicon glyphicon-pencil"></i></a>
        </td>
        <td><a href="/dobavitelji/{{dobavitelj['id']}}/odstrani">
                            <i class="glyphicon glyphicon-trash"></i></a>
        </td>

        
      %end
      </tr>
    </tbody>
  </table>
</div>
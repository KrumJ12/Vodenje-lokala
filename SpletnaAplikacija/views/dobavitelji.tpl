% rebase('osnova.tpl')

<div class="container-fluid">
  <div class="row content">
    <div class="col-sm-3 sidenav">
      <h4>Operacije</h4>
      <ul class="nav nav-pills nav-stacked">

        <li><a href="#section2">Dodaj dobavitelja</a></li>

      </ul><br>

    </div>

    <div class="col-sm-9">



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

      %end
      </tr>
    </tbody>
  </table>
</div>
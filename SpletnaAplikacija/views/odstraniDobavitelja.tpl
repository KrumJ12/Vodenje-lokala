
% rebase('osnova.tpl')
<form method="post">

<div class="container">
  <h1>Želite odstraniti tega dobavitelja in vse njegove pogodbe?</h2>
  <br>

  <h2>Podatki o dobavitelju:</h2>  
   <br>       
  <table class="table table-bordered">
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

      <tr>
        <td>{{dobavitelj['naziv']}}</td>
        <td>{{dobavitelj['naslov']}}</td>
        <td>{{dobavitelj['telefon']}}</td>
        <td>{{dobavitelj['e_posta']}}</td>
        <td>{{dobavitelj['davcna_stevilka']}}</td>
        <td>{{dobavitelj['trr']}}</td>
      </tr>

    </tbody>
  </table>

  <br>
  <h2>Podatki o pogodbah:</h2>  
   <br>
<table class="table table-bordered">
    <thead>
      <tr>
        <th>Ime</th>
        <th>Tip</th>
        <th>Veljavnost</th>
      </tr>
    </thead>
    <tbody>

    % for pogodba in pogodbe:
      <tr>
        <td>{{pogodba['ime']}}</td>
        <td>{{pogodba['tip']}}</td>
        <td>{{pogodba['veljavnost']}}</td>
        
      </tr>
      % end

    </tbody>
  </table>

    <input value="{{dobavitelj['id']}}" name="id_dob" type="hidden">
    <a href="/dobavitelji" class="btn btn-primary">Pojdi nazaj</a>
    <button class="btn btn-danger" type="submit">Odstrani</button>
    
</form>

</div>
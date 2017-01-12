
% rebase('osnova.tpl')
<form method="post">

<div class="container">
  <h1>Želite odstraniti to pogodbo?</h2>
  <br>

  <h2>Podatki o pogodbi:</h2>  
   <br>       
  <table class="table table-bordered">
    <thead>
      <tr>
        <th>Ime pogodbe</th>
        <th>Tip</th>
        <th>Veljavnost do:</th>
        <th>Od dobavitelja št.:</th>
      </tr>
    </thead>
    <tbody>

      <tr>
        <td>{{pogodba['ime']}}</td>
        <td>{{pogodba['tip']}}</td>
        <td>{{pogodba['veljavnost']}}</td>
        <td>{{pogodba['id_dobavitelja']}}</td>
      </tr>

    </tbody>
  </table>


    <input value="{{pogodba['id']}}" name="id_pog" type="hidden">
    <a href="/pogodbe" class="btn btn-primary">Pojdi nazaj</a>
    <button class="btn btn-danger" type="submit">Odstrani</button>
    
</form>
</div>
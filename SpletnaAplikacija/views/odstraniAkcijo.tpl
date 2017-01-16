
% rebase('osnova.tpl')
<form method="post">

<div class="container">
  <h1>Želite odstraniti to akcijo?</h2>
  <br>

  <h2>Podatki o akciji:</h2>  
   <br>       
  <table class="table table-bordered">
    <thead>
      <tr>
        <th>ID izdelka</th>
        <th>Izdelek</th>
        <th>Vrednost akcije:</th>
      </tr>
    </thead>
    <tbody>

      <tr>
        <td>{{akcija['izdelek']}}</td>
        <td>{{izdelki[akcija['izdelek']]['ime']}}</td>
        <td>{{akcija['vrednost']}}</td>
      </tr>

    </tbody>
  </table>


    <input value="{{akcija['id']}}" name="id_akc" type="hidden">
    <a href="/akcije" class="btn btn-primary">Pojdi nazaj</a>
    <button class="btn btn-danger" type="submit">Odstrani</button>
    
</form>
</div>
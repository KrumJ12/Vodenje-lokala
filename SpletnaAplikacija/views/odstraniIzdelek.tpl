
% rebase('osnova.tpl')
<form method="post">

<div class="container">
  <h1>Želite odstraniti ta izdelek?</h2>
  <br>

  <h2>Podatki o izdelku:</h2>  
   <br>       
  <table class="table table-bordered">
    <thead>
      <tr>
        <th>Ime izdelka</th>
        <th>Tip</th>
        <th>Zaloga</th>
        <th>Cena</th>
      </tr>
    </thead>
    <tbody>

      <tr>
        <td>{{izdelek['ime']}}</td>
        <td>{{izdelek['tip']}}</td>
        <td>{{izdelek['zaloga']}}</td>
        <td>{{izdelek['cena']}}</td>
      </tr>

    </tbody>
  </table>


    <input value="{{izdelek['id']}}" name="id_izd" type="hidden">
    <a href="/izdelki" class="btn btn-primary">Pojdi nazaj</a>
    <button class="btn btn-danger" type="submit">Odstrani</button>
    
</form>
</div>
% rebase('osnova.tpl')





<div class="container">

      <h4>Operacije</h4>
      <ul class="nav nav-pills nav-stacked">

        <li><a href="javascript:showhide('uniquename4')">Spremeni vrednost akcije</a></li>

      </ul><br>

  




<form action="/spremeniAkcijo" method="post" id="uniquename4" style="display:none;">

  <div class="form-group">
    <label for="akcija">Akcija</label>
    <select class="form-control" id="akcija" name="akcija">
  %for akcija in seznamAkcij:
      <option>{{akcija['id']}} - {{izdelki[akcija['izdelek']]['ime']}}</option>
  %end
    </select>
  </div>

  <div class="form-group">
    <label for="vrednost">Vrednost akcije</label>
    <input type="text" class="form-control" name = "vrednost" id="vrednost" aria-describedby="emailHelp" placeholder="Vnesi vrednost med 0 in 100">
  </div>


  <button type="submit" class="btn btn-primary">Potrdi</button>

</form>


<div class="container">
  <h2>Tabela trenutno veljavnih akcij:</h2>
  <br>         
  <table class="table">

    <thead>
      <tr>
        <th>ID izdelka</th>
        <th>Izdelek</th>
        <th>Vrednost akcije</th>
        <th>Izbriši</th>
      </tr>
    </thead>

    <tbody>

    % for akcija in seznamAkcij:
      <tr>
        <td>{{akcija['izdelek']}}</td>
        <td>{{izdelki[akcija['izdelek']]['ime']}}</td>
        <td>{{akcija['vrednost']}}</td>
        <td><a href="/akcije/{{akcija['id']}}/odstrani">
                            <i class="glyphicon glyphicon-trash"></i></a></td>
        
      %end
      </tr>
    </tbody>
  </table>
</div>

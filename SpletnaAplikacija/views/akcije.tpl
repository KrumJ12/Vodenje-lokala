% rebase('osnova.tpl')

<div class="container">
  <h2>Tabela trenutno veljavnih akcij:</h2>
  <br>         
  <table class="table">

    <thead>
      <tr>
        <th>ID izdelka</th>
        <th>Izdelek</th>
        <th>Vrednost akcije</th>
        <th>Uredi</th>
        <th>Izbriši</th>
      </tr>
    </thead>

    <tbody>

    % for akcija in seznamAkcij:
      <tr>
        <td>{{akcija['izdelek']}}</td>
        <td>{{izdelki[akcija['izdelek']]['ime']}}</td>
        <td>{{akcija['vrednost']}}</td>
        <td><a href="/akcije/{{akcija['id']}}/uredi">
                            <i class="glyphicon glyphicon-pencil"></i></a></td>
        <td><a href="/akcije/{{akcija['id']}}/odstrani">
                            <i class="glyphicon glyphicon-trash"></i></a></td>
        
      %end
      </tr>
    </tbody>
  </table>
</div>

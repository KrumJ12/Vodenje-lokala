% rebase('osnova.tpl')

<div class="container">
  <h2>Izdani računi:</h2>         
  <table class="table">

    <thead>
      <tr>
        <th>ID računa</th>
        <th>ID natakarja</th>
        <th>Znesek</th>
        <th>Čas nakupa</th>
        <th>Način plačila</th>

      </tr>
    </thead>

    <tbody>

    % for racun in seznam:
      <tr>


        <td>{{racun['id']}}</td>
        <td>{{racun['id_natakarja']}}</td>
        <td>{{racun['znesek']}} €</td>
        <td>{{racun['cas_nakupa']}}</td>
        <td>{{racun['nacin_placila']}}</td>
        
      %end
      </tr>
    </tbody>
  </table>
</div>

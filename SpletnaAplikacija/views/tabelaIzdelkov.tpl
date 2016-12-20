% rebase('osnova.tpl')

<div class="container">
  <h2>Cenik izdelkov</h2>         
  <table class="table">

    <thead>
      <tr>
        <th>Ime</th>
        <th>Tip</th>
        <th>Cena</th>
      </tr>

    </thead>

    <tbody>

%for izdelek in izdelki:
  <tr>
  <td>{{izdelek['ime']}}</td>
  <td>{{izdelek['tip']}}</td>
  <td>{{izdelek['cena']}} €</td>
  </tr>
%end

    </tbody>
  </table>
</div>
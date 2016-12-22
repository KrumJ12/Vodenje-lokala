% rebase('osnova.tpl')

<div class="container-fluid">
  <div class="row content">
    <div class="col-sm-3 sidenav">
      <h4>Operacije</h4>
      <ul class="nav nav-pills nav-stacked">

        <li><a href="#section2">Dodaj pogodbo</a></li>

      </ul><br>

    </div>

    <div class="col-sm-9">



<div class="container">
  <h2>Seznam pogodb</h2>         
  <table class="table">

    <thead>
      <tr>
        <th>ime</th>
        <th>tip</th>
        <th>veljavnost</th>
        <th>id</th>

      </tr>
    </thead>

    <tbody>

    % for pogodba in seznam:
      <tr>


        <td>{{pogodba['ime']}}</td>
        <td>{{pogodba['tip']}}</td>
        <td>{{pogodba['veljavnost']}}</td>
        <td>{{pogodba['id']}}</td>
        

      %end
      </tr>
    </tbody>
  </table>
</div>

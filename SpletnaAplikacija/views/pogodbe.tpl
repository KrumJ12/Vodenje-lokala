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

<form method="post">
  <div class="form-group">
    <label for="ime">Ime pogodbe</label>
    <input type="text" class="form-control" id="ime" name="ime" aria-describedby="emailHelp" placeholder="Vnesi ime pogodbe">
  </div>


  <div class="form-group">
    <label for="tip">Tip</label>
    <select class="form-control" id="tip" name="tip">
      <option>Tip izdelka ni izbran</option>
      <option>topli napitki</option>
      <option>brezalkoholno</option>
      <option>alkoholno</option>
      <option>hrana</option>
      <option>tobak in ostalo</option>
    </select>
  </div>

    <div class="form-group">
    <label for="id_dobavitelja">dobavitelj</label>
    <input type="text" class="form-control" id="id_dobavitelja" name="id_dobavitelja" aria-describedby="emailHelp" placeholder="Izberi dobavitelja "treba spremenit!"">
  </div>


  <div class="form-group">
    <label for="veljavnost">veljavnost</label>
    <input type="text" class="form-control" name = "veljavnost" id="veljavnost" aria-describedby="emailHelp" placeholder="Veljavnost v obliki leto- mesec(2015-09)">
  </div>


  <button type="submit" class="btn btn-primary">Potrdi</button>



</form>

	
<div class="container">
  <h2>Seznam pogodb</h2>         
  <table class="table">

    <thead>
      <tr>
        <th>ime</th>
        <th>tip</th>
        <th>veljavnost</th>
		<th>id_dobavitelja</th>
        <th>id</th>

      </tr>
    </thead>

    <tbody>

    % for pogodba in seznam:
      <tr>


        <td>{{pogodba['ime']}}</td>
        <td>{{pogodba['tip']}}</td>
        <td>{{pogodba['veljavnost']}}</td>
		<td>{{pogodba['id_dobavitelja']}}</td>
        <td>{{pogodba['id']}}</td>
        

      %end
      </tr>
    </tbody>
  </table>
</div>

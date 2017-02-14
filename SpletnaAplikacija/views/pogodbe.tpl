% rebase('osnova.tpl')

<div class="container">
      <h4>Operacije</h4>
      <ul class="nav nav-pills nav-stacked">

        <li><a href="javascript:showhide('uniquename')">Dodaj pogodbo</a></li>

      </ul><br>




<form method="post" id="uniquename" style="display:none;">
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
    <label for="tip">Dobavitelj</label>
    <select class="form-control" id="tip" name="id_dobavitelja">
      <option>Naziv dobavitelja ni izbran</option>
% for ime in imena:
<option>{{ime['naziv']}}</option>
% end

    </select>
  </div>


  <div class="form-group">
    <label for="veljavnost">Veljavnost</label>
    <input type="text" class="form-control" name = "veljavnost" id="veljavnost" aria-describedby="emailHelp" placeholder="Veljavnost v obliki LLLL-MM">
  </div>


  <button type="submit" class="btn btn-primary">Potrdi</button>



</form>
</div>




<div class="container">
  <h2>Seznam pogodb:</h2>  
  <br>      
  <table class="table">

    <thead>
      <tr>
        <th>Ime</th>
        <th>Tip</th>
        <th>Veljavnost</th>
		<th>Dobavitelj</th>
        <th>Uredi</th>
        <th>Izbriši</th>

      </tr>
    </thead>

    <tbody>

    % for pogodba in seznam:
      <tr>
        <td>{{pogodba['ime']}}</td>
        <td>{{pogodba['tip']}}</td>
        <td>{{pogodba['veljavnost']}}</td>
	
        <td>{{pogodba['id_dobavitelja']}} -{{dobavitelji[pogodba['id_dobavitelja']]['naziv']}} </td>
        <td><a href="/pogodbe/{{pogodba['id']}}/uredi">
                            <i class="glyphicon glyphicon-pencil"></i></a></td>
        <td><a href="/pogodbe/{{pogodba['id']}}/odstrani">
                            <i class="glyphicon glyphicon-trash"></i></a></td>
     %end  
      </tr>

    </tbody>
  </table>
</div>

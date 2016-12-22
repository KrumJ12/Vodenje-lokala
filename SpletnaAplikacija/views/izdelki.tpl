% rebase('osnova.tpl')

<div class="container-fluid">
  <div class="row content">
    <div class="col-sm-3 sidenav">
      <h4>Operacije</h4>
      <ul class="nav nav-pills nav-stacked">

        <li><a href="javascript:showhide('uniquename')">Dodaj izdelek</a></li>
        <li><a href="javascript:showhide('uniquename2')">Spremeni ceno</a></li>
		<li><a href="javascript:showhide('uniquename3')">Dodaj zalogo</a></li>

      </ul><br>

    </div>

    <div class="col-sm-9">



<form method="post" id="uniquename" style="display:none;">
  <div class="form-group">
    <label for="ime">Ime izdelka</label>
    <input type="text" class="form-control" id="ime" name="ime" aria-describedby="emailHelp" placeholder="Vnesi ime izdelka">
  </div>


  <div class="form-group">
    <label for="zaloga">Zaloga</label>
    <input type="text" class="form-control" name = "zaloga" id="zaloga" aria-describedby="emailHelp" placeholder="Vnesi količino, npr: 30">
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
    <label for="cena">Cena</label>
    <input type="text" class="form-control" name = "cena" id="cena" aria-describedby="emailHelp" placeholder="Vnesi ceno npr: 1.8">
  </div>


  <button type="submit" class="btn btn-primary">Potrdi</button>



</form>
</div>

 <div class="col-sm-9">
<form action="/spremeniCeno" method="post" id="uniquename2" style="display:none;">

  <div class="form-group">
    <label for="izdelek">Izdelek</label>
    <select class="form-control" id="tip" name="izdelek">
	%for izdelek in imena:
      <option>{{izdelek['ime']}}</option>
	%end
    </select>
  </div>

  <div class="form-group">
    <label for="cena">Cena</label>
    <input type="text" class="form-control" name = "cena" id="cena" aria-describedby="emailHelp" placeholder="Vnesi ceno npr: 1.8">
  </div>


  <button type="submit" class="btn btn-primary">Potrdi</button>



</form>
  </div>
  
 <div class="col-sm-9">
<form action="/dodajZalogo" method="post" id="uniquename3" style="display:none;">

  <div class="form-group">
    <label for="izdelek">Izdelek</label>
    <select class="form-control" id="tip" name="izdelek">
	%for izdelek in imena:
      <option>{{izdelek['ime']}}</option>
	%end
    </select>
  </div>

  <div class="form-group">
    <label for="zaloga">Zaloga</label>
    <input type="text" class="form-control" name = "zaloga" id="zaloga" aria-describedby="emailHelp" placeholder="Vnesi zalogo">
  </div>


  <button type="submit" class="btn btn-primary">Potrdi</button>



</form>
  </div>
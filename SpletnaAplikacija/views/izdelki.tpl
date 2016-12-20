% rebase('osnova.tpl')

<div class="container-fluid">
  <div class="row content">
    <div class="col-sm-3 sidenav">
      <h4>Operacije</h4>
      <ul class="nav nav-pills nav-stacked">

        <li><a href="#section2">Dodaj izdelek</a></li>
        <li><a href="#section3">Spremeni ceno</a></li>

      </ul><br>

    </div>

    <div class="col-sm-9">



<form>
  <div class="form-group">
    <label for="exampleInputEmail1">Ime izdelka</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Vnesi ime izdelka">
  </div>


  <div class="form-group">
    <label for="exampleInputEmail1">Zaloga</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Vnesi količino, npr: 30">
  </div>


  <div class="form-group">
    <label for="exampleSelect1">Tip</label>
    <select class="form-control" id="exampleSelect1">
      <option>Tip izdelka ni izbran</option>
      <option>Topli napitek</option>
      <option>Brezalkoholna pijača</option>
      <option>Alkoholna pijača</option>
      <option>Hrana</option>
      <option>Tobak in ostalo</option>
    </select>
  </div>

  <div class="form-group">
    <label for="exampleInputEmail1">Cena</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Vnesi ceno npr: 1.8">
  </div>


  <button type="submit" class="btn btn-primary">Potrdi</button>



</form>
  </div>
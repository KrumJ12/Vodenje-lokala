% rebase('osnova.tpl')
<form method="post">

    <div class="form-group">
        <label for="ime">Ime izdelka</label>
        <input value="{{izdelek['ime']}}" placeholder="Ime izdelka" name="ime" type="text" class="form-control">
    </div>

  	<div class="form-group">
	    <label for="tip">Tip izdelka</label>
	    <select value="{{izdelek['tip']}}" class="form-control" id="tip" name="tip">
	      <option>Tip izdelka ni izbran</option>
	      <option>topli napitki</option>
	      <option>brezalkoholno</option>
	      <option>alkoholno</option>
	      <option>hrana</option>
	      <option>tobak in ostalo</option>
	    </select>
  	</div>

    <div class="form-group">
        <label for="zaloga">Zaloga izdelka:</label>
        <input value="{{izdelek['zaloga']}}" placeholder="200" name="zaloga" type="text" class="form-control">
    </div>

    <div class="form-group">
        <label for="cena">Cena</label>
        <input value="{{izdelek['cena']}}" placeholder="200" name="cena" type="text" class="form-control">
    </div>

    <input value="{{izdelek['id']}}" name="id_izd" type="hidden">
    <button class="btn btn-primary" type="submit">Spremeni</button>
    
</form>
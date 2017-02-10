
% rebase('osnova.tpl')
<form method="post">

    <div class="form-group">
        <label for="ime">Ime pogodbe</label>
        <input value="{{pogodba['ime']}}" placeholder="Ime izdelka" name="ime" type="text" class="form-control">
    </div>

    <div class="form-group">
        <label for="tip">Tip pogodbe</label>
        <input value="{{pogodba['tip']}}" placeholder="hrana/pijaca/ostalo/..." name="tip" type="text" class="form-control">
    </div>

    <div class="form-group">
        <label for="veljavnost">Veljavnost do</label>
        <input value="{{pogodba['veljavnost']}}" placeholder="2017-10" name="veljavnost" type="text" class="form-control">
    </div>


    <input value="{{pogodba['id']}}" name="id_pog" type="hidden">
    <button class="btn btn-primary" type="submit">Spremeni</button>
    
</form>
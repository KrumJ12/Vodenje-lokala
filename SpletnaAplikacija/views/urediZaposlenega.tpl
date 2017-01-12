
% rebase('osnova.tpl')
<form method="post">
    <div class="form-group">
        <label for="ime">Ime</label>
        <input value="{{zaposlen['ime']}}" placeholder="Janez" name="ime" type="text" class="form-control">
        
    </div>
    <div class="form-group">
        <label for="priimek">Priimek</label>
        <input value="{{zaposlen['priimek']}}" placeholder="Novak" name="priimek" type="text" class="form-control">
        
    </div>
    <div class="form-group">
        <label for="datum_rojstva">Datum rojstva</label>
        <input value="{{zaposlen['datum_rojstva']}}" placeholder="1981-10-11" name="datum_rojstva" type="text" class="form-control">
        
    </div>
    <div class="form-group">
        <label for="e_posta">Elektronska pošta</label>
        <input value="{{zaposlen['e_posta']}}" placeholder="janez.novak@fmf.uni-lj.si" name="e_posta" type="text" class="form-control">
        
    </div>
    <div class="form-group">
        <label for="funkcija">Funkcija</label>
        <input value="{{zaposlen['funkcija']}}" placeholder="1" name="funkcija" type="text" class="form-control">
        
    </div>
    <div class="form-group">
        <label for="datum_zaposlitve">Datum zaposlitve</label>
        <input value="{{zaposlen['datum_zaposlitve'] or ''}}" placeholder="2016-01-01" name="datum_zaposlitve" type="text" class="form-control">
        
    </div>
    <div class="form-group">
        <label for="telefon">Telefon</label>
        <input value="{{zaposlen['telefon']}}" placeholder="051 270 584" name="telefon" type="text" class="form-control">
       
    </div>
    <div class="form-group">
        <label for="prebivalisce">Prebivališče</label>
        <input value="{{zaposlen['prebivalisce']}}" placeholder="Novakova ulica 11" name="prebivalisce" type="text" class="form-control">
        
    </div>
    <input value="{{zaposlen['id']}}" name="id_zap" type="hidden">
    <button class="btn btn-primary" type="submit">Spremeni</button>
</form>
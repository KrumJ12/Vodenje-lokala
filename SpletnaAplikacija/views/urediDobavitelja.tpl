
% rebase('osnova.tpl')
<form method="post">

    <div class="form-group">
        <label for="naziv">Naziv</label>
        <input value="{{dobavitelj['naziv']}}" placeholder="Pekarna d.o.o." name="naziv" type="text" class="form-control">
    </div>

    <div class="form-group">
        <label for="naslov">Naslov</label>
        <input value="{{dobavitelj['naslov']}}" placeholder="Pekarniška ulica 11" name="naslov" type="text" class="form-control">
    </div>

    <div class="form-group">
        <label for="telefon">Telefon</label>
        <input value="{{dobavitelj['telefon']}}" placeholder="051 000 999" name="telefon" type="text" class="form-control">
    </div>

    <div class="form-group">
        <label for="e_posta">Elektronska pošta</label>
        <input value="{{dobavitelj['e_posta']}}" placeholder="pekarna@gmail.com" name="e_posta" type="text" class="form-control">
    </div>

    <div class="form-group">
        <label for="davcna">Davčna številka</label>
        <input value="{{dobavitelj['davcna_stevilka']}}" placeholder="12345678" name="davcna" type="text" class="form-control">
    </div>

    <div class="form-group">
        <label for="trr">Transakcijski račun</label>
        <input value="{{dobavitelj['trr']}}" placeholder="SI56 8062 7293 9999 780" name="trr" type="text" class="form-control">
    </div>

    <input value="{{dobavitelj['id']}}" name="id_dob" type="hidden">
    <button class="btn btn-primary" type="submit">Spremeni</button>
    
</form>
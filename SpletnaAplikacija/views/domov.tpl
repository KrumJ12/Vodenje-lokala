% rebase('osnova.tpl')

<div class="row">

<div class="col-xs-6">



  <h1>Vnesi račun:</h1><hr>
  <table id = "mojaT" class="table table-striped table-hover table-bordered">
        <tbody>
            <tr>
                <th>Izdelek</th>
                <th>Količina</th>
                <th>Cena enega</th>
                <th>Skupna cena</th>
            </tr>


            <tr>
            <tr>
                <th colspan="3"><span class="pull-right">Skupaj</span></th>
                <th>končna cena €</th>
            </tr>
            <tr>
                <td><a href="#" class="btn btn-primary">Izprazni</a></td>
                <td colspan="3"><a href="#" class="pull-right btn btn-success">Potrdi nakup</a></td>
            </tr>
        </tbody>
    </table>          
      
</div>




<script>
function dodajVrstico(ime,cena) {
    var table = document.getElementById("mojaT");
    var row = table.insertRow(1);

    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    cell1.innerHTML = ime;
    cell2.innerHTML = "1x";
    cell3.innerHTML = cena;
    cell4.innerHTML = "skupna";
}
</script>



  <div class="col-xs-6">
    
% for ime in imena:
<a onclick="dodajVrstico(this.name,this.id)" id = {{ime['cena']}} name={{ime['ime']}} class="btn btn-default btn-sm">{{ime['ime']}}</a>
% end


  </div>




</div>
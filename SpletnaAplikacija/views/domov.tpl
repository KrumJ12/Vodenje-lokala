% rebase('osnova.tpl')

<div class="row">

<div class="col-xs-6">



  <h1>Vnesi račun:</h1><hr>
  <table id = "mojaT" class="table table-striped table-hover table-bordered">
        <tbody>
            <tr>
                <th>Izdelek</th>
                <th>Količina</th>
                <th>Cena</th>
            </tr>


            <tr>
            <tr>
                <th colspan="3"><span class="pull-right">Skupaj</span></th>
            </tr>
            <tr>
                <td><a href="#" class="btn btn-primary">Izprazni</a></td>
                <td colspan="3"><a href="#" class="pull-right btn btn-success">Potrdi nakup</a></td>
            </tr>
        </tbody>
    </table>          
      
</div>




  <div class="col-xs-6">
    {{izdelki}}
% for ime in imena:
<a href="/?{{stari_niz}}&id={{ime['id']}}" class="btn btn-default btn-sm">{{ime['ime']}}</a>
% end


  </div>




</div>
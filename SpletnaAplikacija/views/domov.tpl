% rebase('osnova.tpl')



<div class="row">

<div class="col-xs-6">



  <h1>Vnesi račun:</h1><hr>



<a href="/?{{link}}&nacin=1">
 Gotovina</a>
 <br>
<a href="/?{{link}}&nacin=2">
 Kartica</a>
 <br>
 <a href="/?{{link}}&nacin=3">
 Dobavnica</a>
<br><br>
<table class="table table-striped table-hover table-bordered">

    <thead>
      <tr>
      
        <th>Izdelek</th>
        <th>Cena</th>
      </tr>
    </thead>

    <tbody>

            % for el in izdelki:
            <tr>
            % if el != '':
            <td>{{imena[el][1]}}</td>
            <td>{{imena[el][4]}}</td>
            %end
            % end
</tr>
    </tbody>

 <th>Skupaj</th>
<th> 

{{round(sum(imena[x][4] for x in izdelki),2)}}


 </th>
 <tr>
 <td>
     <a href="/" type="submit" class="btn btn-primary">Izprazni račun</a>
 </td>
 <td>
   <a href="/{{plac}}&{{link}}" class="btn btn-primary">Zaključi račun</a>
 </td>
 </tr>
  </table>


        


</div>


  <div class="col-xs-6">
    <br>
  
% for ime in imena.values():
% if ime['tip'] == 'topli napitki':
<a href="/?{{plac}}&{{link}}&id={{ime['id']}}" class="btn btn-default btn-sm">{{ime['ime']}}</a>
% end
% if ime['tip'] == 'alkoholno':
<a href="/?{{plac}}&{{link}}&id={{ime['id']}}" class="btn btn-danger btn-sm">{{ime['ime']}}</a>
% end
% if ime['tip'] == 'brezalkoholno':
<a href="/?{{plac}}&{{link}}&id={{ime['id']}}" class="btn btn-primary btn-sm">{{ime['ime']}}</a>
% end
% if ime['tip'] == 'hrana':
<a href="/?{{plac}}&{{link}}&id={{ime['id']}}" class="btn btn-warning btn-sm">{{ime['ime']}}</a>
% end
% else:
<a href="/?{{plac}}&{{link}}&id={{ime['id']}}" class="btn btn-info btn-sm">{{ime['ime']}}</a>
% end
% end

	
  </div>




</div>
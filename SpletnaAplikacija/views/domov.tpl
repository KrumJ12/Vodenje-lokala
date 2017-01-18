% rebase('osnova.tpl')



<div class="row">

<div class="col-xs-6">



  <h1>Vnesi račun:</h1><hr>

<form method="post" action="/noviRacun">


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
            <td>
            	{{imena[el][1]}}
            	<input name="izdelek" type="hidden" value="{{el}}">
            </td>
            <td>{{imena[el][4]}}</td>
            %end
            % end
</tr>
    </tbody>

 <th>Skupaj</th>
<th> 

<input name="znesek" type="text" value="{{round(sum(imena[x][4] for x in izdelki),2)}}">
<input name="znesek" type="text" value="{{znesek}}">

 </th>
  </table>
  <br>

<h2>Izberi način plačila:</h2>
<br>
<label class="radio-inline"><input type="radio" value="1" name="placilo" checked >Gotovina</label>
<label class="radio-inline"><input type="radio" value="2" name="placilo">Kartica</label>
<label class="radio-inline"><input type="radio" value="3" name="placilo">Dobavnica</label>
<br><br><br>
 <button type="submit" class="btn btn-primary">Zaključi račun</button>

</form>
        


</div>


  <div class="col-xs-6">
    <br>
  
% for ime in imena.values():
% if ime['tip'] == 'topli napitki':
<a href="/?{{plac}}&{{link}}&id={{ime['id']}}" class="btn btn-default btn-sm">{{ime['ime']}}</a>

% elif ime['tip'] == 'alkoholno':
<a href="/?{{plac}}&{{link}}&id={{ime['id']}}" class="btn btn-danger btn-sm">{{ime['ime']}}</a>

% elif ime['tip'] == 'brezalkoholno':
<a href="/?{{plac}}&{{link}}&id={{ime['id']}}" class="btn btn-primary btn-sm">{{ime['ime']}}</a>

% elif ime['tip'] == 'hrana':
<a href="/?{{plac}}&{{link}}&id={{ime['id']}}" class="btn btn-warning btn-sm">{{ime['ime']}}</a>

% else:
<a href="/?{{plac}}&{{link}}&id={{ime['id']}}" class="btn btn-info btn-sm">{{ime['ime']}}</a>
% end
% end

	
  </div>




</div>
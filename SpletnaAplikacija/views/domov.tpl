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
        <th>Akcijska cena</th>
      </tr>
    </thead>

    <tbody>
            % for izdelek in izdelki:
            <tr>
            % if izdelek != '':
            <td>
            	{{imena[izdelek-1][1]}}
            	<input name="izdelek" type="hidden" value="{{izdelek}}">
            </td>
            <td>{{imena[izdelek-1][4]}} €</td>
            % if akcija[izdelek-1] == '/':
            <td> {{akcija[izdelek-1]}} </td>
            % else :
            <td>{{akcija[izdelek-1]}} €</td>

            % end
            %end
            % end
</tr>
    </tbody>

 <th>Skupaj</th>
<th> 
 <label>
<input name="znesek2" type="hidden" value="{{round(sum(imena[x-1][4] for x in izdelki),2)}}">{{round(sum(imena[izdelek-1][4] for izdelek in izdelki),2)}} €
</label>

 </th>
 <th>
 <label><input name="znesek" type="hidden" value="{{znesek}}">{{znesek}} €</label>
 </th>
  </table>
  <br>

<h2>Izberi način plačila:</h2>
<br>
<label class="radio-inline"><input type="radio" value="1" name="placilo" checked >Gotovina</label>
<label class="radio-inline"><input type="radio" value="2" name="placilo">Kartica</label>
<label class="radio-inline"><input type="radio" value="3" name="placilo">Dobavnica</label>
<br><br>

<h3>Natakar:</h3>

% for natakar in natakarji:
<label class="radio-inline"><input type="radio" value="{{natakar['id']}}" name="id_nat">{{natakar['id']}}</label>
% end

<br><br><br>
 <button type="submit" class="btn btn-primary">Zaključi račun</button>

</form>
        


</div>


  <div class="col-xs-6">
    <br>
  
% for ime in imenaTIP:
% if ime['tip'] == 'topli napitki':
<a href="/?{{plac}}&{{link}}&id={{ime['id']}}" class="btn btn-default btn-xs">{{ime['ime']}}</a>

% elif ime['tip'] == 'alkoholno':
<a href="/?{{plac}}&{{link}}&id={{ime['id']}}" class="btn btn-danger btn-xs">{{ime['ime']}}</a>

% elif ime['tip'] == 'brezalkoholno':
<a href="/?{{plac}}&{{link}}&id={{ime['id']}}" class="btn btn-primary btn-xs">{{ime['ime']}}</a>

% elif ime['tip'] == 'hrana':
<a href="/?{{plac}}&{{link}}&id={{ime['id']}}" class="btn btn-warning btn-xs">{{ime['ime']}}</a>

% else:
<a href="/?{{plac}}&{{link}}&id={{ime['id']}}" class="btn btn-info btn-xs">{{ime['ime']}}</a>
% end
% end

	
  </div>




</div>
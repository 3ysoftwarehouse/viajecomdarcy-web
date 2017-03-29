$(document).ready(function() {

    $("#id_id_opcional").select2();
    $('#id_data_prevista').mask("99/99/9999");

    $(function() {

      $('#id_cidade_table .tr').formset({
          prefix: '{{ cidadeformset.prefix }}'
      });
      $('#id_acomodacao_table .tr').formset({
          prefix: '{{ acomodacaoformset.prefix }}'
      });
      $(".acomodacao").focus(function(){
        aux_select(this.value, this.options[this.selectedIndex].text)
      });
      $(".acomodacao").change(function(){
        check_select('update');
      });
      $(".add-row").click(function(){
        check_select('add');
      });

    });

  });

  function aux_select(value, text){
    document.getElementById("select_aux").innerHTML = value + "|" + text
  }

  function check_select(type){
    var selects = document.getElementsByClassName("acomodacao");
    console.log(type)

    // UPDATE OR DELETE
    if(type == 'update' || type == 'delete'){
      
      var aux = document.getElementById("select_aux").innerHTML.split('|')
      var element = document.createElement("option")
      element.value = aux[0]
      element.text = aux[1]

      for(x=0;x<selects.length;x++){
        var select = selects[x]
        var search = false
        for(y=0;y<select;y++){
          var option = select[y]
          if(option.text == element.text){
            console.log(true)
            search = true
            break
          }
        }
        if(!search && selects.length>1){
          console.log(false)
          select.add(element)
        }
      }

    }else{

      for(x=0;x<selects.length;x++){
        if(selects[x].selectedIndex != 0){
          var element = selects[x][selects[x].selectedIndex]
          for(y=x+1;y<selects.length;y++){
            var select = selects[y]
            for(z=0;z<select.length;z++){
              var option = select[z]
              if(option.text == element.text){
                select.remove(option.index)
                break
              }
            }
          }
        }
      }

    }
  }
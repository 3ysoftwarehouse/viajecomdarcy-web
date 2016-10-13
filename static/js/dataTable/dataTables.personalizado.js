$(document).ready(function() {
    $('#datatable').DataTable( {
        destroy: true,
        "language": {
        "lengthMenu": 'Exibir <select>'+
       '<option value="10">10</option>'+
       '<option value="20">20</option>'+
       '<option value="30">30</option>'+
       '<option value="40">40</option>'+
       '<option value="50">50</option>'+
       '<option value="-1">Todos</option>'+ 
       '</select> Registros',
        "zeroRecords": "Não há registros para exibir",
        "info": "Mostrando  _PAGE_ de _PAGES_ paginas" ,   
        "infoEmpty": "Não há entradas para mostrar",
         "emptyTable": "Não há dados disponíveis na tabela",
        "search":         "Busca:",
        "paginate": {
        "next": "Próximo",
        "previous": "Anterior",

        }
      },


        "dom": 'T<"clear">lfrtip',
        "tableTools": {
            "sSwfPath": "/viajecomdarcy-web/static/js/dataTable/copy_csv_xls_pdf.swf",
            "aButtons": [
                "copy",
                "print",
                {
                    "sExtends":    "collection",
                    "sButtonText": "Salvar",
                    "aButtons":    [ "csv", "xls", "pdf" ]
                }
            ]
        }
    } );
} );

$(document).ready(function() {
    $('#datatable2').DataTable( {
        destroy: true,
        "language": {
        "lengthMenu": 'Exibir <select>'+
       '<option value="10">10</option>'+
       '<option value="20">20</option>'+
       '<option value="30">30</option>'+
       '<option value="40">40</option>'+
       '<option value="50">50</option>'+
       '<option value="-1">Todos</option>'+ 
       '</select> Registros',
        "zeroRecords": "Não há registros para exibir",
        "info": "Mostrando  _PAGE_ de _PAGES_ paginas" ,   
        "infoEmpty": "Não há entradas para mostrar",
         "emptyTable": "Não há dados disponíveis na tabela",
        "search":         "Busca:",
        "paginate": {
        "next": "Próximo",
        "previous": "Anterior",

        }
      },


        "dom": 'T<"clear">lfrtip',
        "tableTools": {
            "sSwfPath": "/viajecomdarcy-web/static/js/dataTable/copy_csv_xls_pdf.swf",
            "aButtons": [
                "copy",
                "print",
                {
                    "sExtends":    "collection",
                    "sButtonText": "Salvar",
                    "aButtons":    [ "csv", "xls", "pdf" ]
                }
            ]
        }
    } );
} );


$(document).ready(function() {
    $('#datatable3').DataTable( {
        destroy: true,
        "language": {
        "lengthMenu": 'Exibir <select>'+
       '<option value="10">10</option>'+
       '<option value="20">20</option>'+
       '<option value="30">30</option>'+
       '<option value="40">40</option>'+
       '<option value="50">50</option>'+
       '<option value="-1">Todos</option>'+
       '</select> Registros',
        "zeroRecords": "Não há registros para exibir",
        "info": "Mostrando  _PAGE_ de _PAGES_ paginas" ,
        "infoEmpty": "Não há entradas para mostrar",
         "emptyTable": "Não há dados disponíveis na tabela",
        "search":         "Busca:",
        "paginate": {
        "next": "Próximo",
        "previous": "Anterior",

        }
      },


        "dom": 'T<"clear">lfrtip',
        "tableTools": {
            "sSwfPath": "/viajecomdarcy-web/static/js/dataTable/copy_csv_xls_pdf.swf",
            "aButtons": [
                "copy",
                "print",
                {
                    "sExtends":    "collection",
                    "sButtonText": "Salvar",
                    "aButtons":    [ "csv", "xls", "pdf" ]
                }
            ]
        }
    } );
} );


$(document).ready(function() {
    $('#datatable4').DataTable( {
        "language": {
        "lengthMenu": 'Exibir <select>'+
       '<option value="10">10</option>'+
       '<option value="20">20</option>'+
       '<option value="30">30</option>'+
       '<option value="40">40</option>'+
       '<option value="50">50</option>'+
       '<option value="-1">Todos</option>'+
       '</select> Registros',
        "zeroRecords": "Não há registros para exibir",
        "info": "Mostrando  _PAGE_ de _PAGES_ paginas" ,
        "infoEmpty": "Não há entradas para mostrar",
         "emptyTable": "Não há dados disponíveis na tabela",
        "search":         "Busca:",
        "paginate": {
        "next": "Próximo",
        "previous": "Anterior",

        }
      },


        "dom": 'T<"clear">lfrtip',
        "tableTools": {
            "sSwfPath": "/viajecomdarcy-web/static/js/dataTable/copy_csv_xls_pdf.swf",
            "aButtons": [
                "copy",
                "print",
                {
                    "sExtends":    "collection",
                    "sButtonText": "Salvar",
                    "aButtons":    [ "csv", "xls", "pdf" ]
                }
            ]
        }
    } );
} );

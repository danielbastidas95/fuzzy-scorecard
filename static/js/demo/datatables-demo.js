// Call the dataTables jQuery plugin
/*
$(document).ready(function() {
  $('#dataTable').DataTable();
});
*/

$(document).ready(function(){
  $.ajax({
      type: 'GET',
      url:'/databscacc',
      dataType: 'text',
      contentType:'charset=utf-8',
      success: function(response){
          var datos = JSON.parse(response);
          console.log(datos)
          console.log(datos[1]);
          console.log(datos.length);
          $('#example').DataTable({
            "scrollX": true,
            "scrollY": true,
            data: datos,
            columns: [
                {title: "Id" },
                {title: "Objetivo estratégico"},
                {title: "Iniciativa"},
                {title: "Accion"},
                {title: "Meta"},
                {title: "Enero"},
                {title: "Febrero"},
                {title: "Marzo"},
                {title: "Abril"},
                {title: "Mayo"},
                {title: "Junio"},
                {title: "Julio"},
                {title: "Agosto"},
                {title: "Septiembre"},
                {title: "Octubre"},
                {title: "Noviembre"},
                {title: "Diciembre"},
                {title: "Cumplimiento"}
            ]
          });

          var table = $('#example').DataTable();
 
          $('#example tbody').on( 'click', 'tr', function () {
              if ( $(this).hasClass('selected') ) {
                  $(this).removeClass('selected');
                  //console.log(table.rows( { selected: true } ).data())
                  //console.log(table.rows('.selected').data);
                  //console.log(table.row('.selected').data());
                  //console.log($(this));
                  
              }
              else {
                  table.$('tr.selected').removeClass('selected');
                  $(this).addClass('selected');
                  //console.log(table.rows( { selected: true } ).data())
                  //console.log(table.rows('.selected').data);
                  //console.log(table.row('.selected').data());
                  //console.log($(this));

              }
          } );
      
          $('#button').click( function () {
              var datarow = table.row('.selected').data();

              pos = parseInt(datarow[0]);

              console.log(datarow)
              console.log(pos);

              document.getElementById("posicion").value = datarow[0];
              $("#posicion").hide();
              

              document.getElementById("staticBackdropLabel").innerHTML = datarow[1];
              document.getElementById("iniciativa").innerHTML = datarow[2];
              document.getElementById("accion").innerHTML = datarow[3];
              document.getElementById("meta").innerHTML = datarow[4] + "%";
              document.getElementById("enero").value = datarow[5];
              document.getElementById("febrero").value = datarow[6];
              document.getElementById("marzo").value = datarow[7];
              document.getElementById("abril").value = datarow[8];
              document.getElementById("mayo").value = datarow[9];
              document.getElementById("junio").value = datarow[10];
              document.getElementById("julio").value = datarow[11];
              document.getElementById("agosto").value = datarow[12];
              document.getElementById("septiembre").value = datarow[13];
              document.getElementById("octubre").value = datarow[14];
              document.getElementById("noviembre").value = datarow[15];
              document.getElementById("diciembre").value = datarow[16];
              document.getElementById("cumplimiento").innerHTML = datarow[17] + "%";

              //table.row('.selected').remove().draw( false );
          } );


      },
      error: function(e){
          console.log(e);
      }
  });
});

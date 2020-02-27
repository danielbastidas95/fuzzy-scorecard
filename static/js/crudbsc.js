$(document).ready(function(){
    $.ajax({
        type: 'GET',
        url:'/databscacc',
        dataType: 'text',
        contentType:'charset=utf-8',
        success: function(response){
            var datos = JSON.parse(response);
            console.log(datos[1]);
            console.log(datos.length);
            /*
            var datos_tabla = datos
            var filas = 7
            var columnas = 14

            for(var n=1; n<filas; n++){

            }

            */
            
            $('#example').DataTabe({
                data: datos,
                columns: [
                    {title: "Objetivo estratégico" },
                    {title: "Iniciativa"},
                    {title: "Accion"},
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
                    {title: "noviembre"},
                    {title: "Diciembre"}
                ]
            });
        },
        error: function(e){
            console.log(e);
        }
    });
});
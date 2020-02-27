$(document).ready(function(){
    $.ajax({
        type: 'GET',
        url:'/data-inic-json',
        dataType: 'text',
        contentType:'charset=utf-8',
        success: function (response){
            var datos = JSON.parse(response);
            var inic1_value = parseInt(datos[1][1]);
            var inic2_value = parseInt(datos[2][1]);
            var inic3_value = parseInt(datos[3][1]);
            var inic4_value = parseInt(datos[4][1]);
            var inic5_value = parseInt(datos[5][1]);
            var inic6_value = parseInt(datos[6][1]);
            var inic7_value = parseInt(datos[7][1]);
            var inic8_value = parseInt(datos[8][1]);
            var inic9_value = parseInt(datos[9][1]);
            var inic10_value = parseInt(datos[10][1]);
            var inic11_value = parseInt(datos[11][1]);
            var inic12_value = parseInt(datos[12][1]);
            var inic13_value = parseInt(datos[13][1]);
            var inic14_value = parseInt(datos[14][1]);
            var inic15_value = parseInt(datos[15][1]);
            var inic16_value = parseInt(datos[16][1]);
            var inic17_value = parseInt(datos[17][1]);
            var inic18_value = parseInt(datos[18][1]);
            var inic19_value = parseInt(datos[19][1]);

            //put value inic
            document.getElementById("value_1_1").innerHTML= inic1_value + "%";
            if(inic1_value <= 50){
                var x = document.getElementById("bar_ini_1_1");
                x.className = "progress-bar bg-danger";
                x.style.width = inic1_value+"%";
            } else if (inic1_value >50 & inic1_value <80){
                var x = document.getElementById("bar_ini_1_1");
                x.className = "progress-bar bg-warning";
                x.style.width = inic1_value+"%";
            } else{
                var x = document.getElementById("bar_ini_1_1");
                x.className = "progress-bar bg-success";
                x.style.width = inic1_value+"%";
            }

            document.getElementById("value_1_2").innerHTML= inic2_value + "%";
            if(inic2_value <= 50){
                var x = document.getElementById("bar_ini_1_2");
                x.className = "progress-bar bg-danger";
                x.style.width = inic2_value+"%";
            } else if (inic2_value >50 & inic2_value <80){
                var x = document.getElementById("bar_ini_1_2");
                x.className = "progress-bar bg-warning";
                x.style.width = inic2_value+"%";
            } else{
                var x = document.getElementById("bar_ini_1_2");
                x.className = "progress-bar bg-success";
                x.style.width = inic2_value+"%";
            }

            document.getElementById("value_2_1").innerHTML= inic3_value + "%";
            if(inic3_value <= 50){
                var x = document.getElementById("bar_ini_2_1");
                x.className = "progress-bar bg-danger";
                x.style.width = inic3_value+"%";
            } else if (inic3_value >50 & inic3_value <80){
                var x = document.getElementById("bar_ini_2_1");
                x.className = "progress-bar bg-warning";
                x.style.width = inic3_value+"%";
            } else{
                var x = document.getElementById("bar_ini_2_1");
                x.className = "progress-bar bg-success";
                x.style.width = inic3_value+"%";
            }

            document.getElementById("value_2_2").innerHTML= inic4_value + "%";
            if(inic4_value <= 50){
                var x = document.getElementById("bar_ini_2_2");
                x.className = "progress-bar bg-danger";
                x.style.width = inic4_value+"%";
            } else if (inic4_value >50 & inic4_value <80){
                var x = document.getElementById("bar_ini_2_2");
                x.className = "progress-bar bg-warning";
                x.style.width = inic4_value+"%";
            } else{
                var x = document.getElementById("bar_ini_2_2");
                x.className = "progress-bar bg-success";
                x.style.width = inic4_value+"%";
            }

            document.getElementById("value_2_3").innerHTML= inic5_value + "%";
            if(inic5_value <= 50){
                var x = document.getElementById("bar_ini_2_3");
                x.className = "progress-bar bg-danger";
                x.style.width = inic5_value+"%";
            } else if (inic5_value >50 & inic5_value <80){
                var x = document.getElementById("bar_ini_2_3");
                x.className = "progress-bar bg-warning";
                x.style.width = inic5_value+"%";
            } else{
                var x = document.getElementById("bar_ini_2_3");
                x.className = "progress-bar bg-success";
                x.style.width = inic5_value+"%";
            }

            document.getElementById("value_3_1").innerHTML= inic6_value + "%";
            if(inic6_value <= 50){
                var x = document.getElementById("bar_ini_3_1");
                x.className = "progress-bar bg-danger";
                x.style.width = inic6_value+"%";
            } else if (inic6_value >50 & inic6_value <80){
                var x = document.getElementById("bar_ini_3_1");
                x.className = "progress-bar bg-warning";
                x.style.width = inic6_value+"%";
            } else{
                var x = document.getElementById("bar_ini_3_1");
                x.className = "progress-bar bg-success";
                x.style.width = inic6_value+"%";
            }

            document.getElementById("value_4_1").innerHTML= inic7_value + "%";
            if(inic7_value <= 50){
                var x = document.getElementById("bar_ini_4_1");
                x.className = "progress-bar bg-danger";
                x.style.width = inic7_value+"%";
            } else if (inic7_value >50 & inic7_value <80){
                var x = document.getElementById("bar_ini_4_1");
                x.className = "progress-bar bg-warning";
                x.style.width = inic7_value+"%";
            } else{
                var x = document.getElementById("bar_ini_4_1");
                x.className = "progress-bar bg-success";
                x.style.width = inic7_value+"%";
            }

            document.getElementById("value_4_2").innerHTML= inic8_value + "%";
            if(inic8_value <= 50){
                var x = document.getElementById("bar_ini_4_2");
                x.className = "progress-bar bg-danger";
                x.style.width = inic8_value+"%";
            } else if (inic8_value >50 & inic8_value <80){
                var x = document.getElementById("bar_ini_4_2");
                x.className = "progress-bar bg-warning";
                x.style.width = inic8_value+"%";
            } else{
                var x = document.getElementById("bar_ini_4_2");
                x.className = "progress-bar bg-success";
                x.style.width = inic8_value+"%";
            }

            document.getElementById("value_4_3").innerHTML= inic9_value + "%";
            if(inic9_value <= 50){
                var x = document.getElementById("bar_ini_4_3");
                x.className = "progress-bar bg-danger";
                x.style.width = inic9_value+"%";
            } else if (inic9_value >50 & inic9_value <80){
                var x = document.getElementById("bar_ini_4_3");
                x.className = "progress-bar bg-warning";
                x.style.width = inic9_value+"%";
            } else{
                var x = document.getElementById("bar_ini_4_3");
                x.className = "progress-bar bg-success";
                x.style.width = inic9_value+"%";
            }

            document.getElementById("value_4_4").innerHTML= inic10_value + "%";
            if(inic10_value <= 50){
                var x = document.getElementById("bar_ini_4_4");
                x.className = "progress-bar bg-danger";
                x.style.width = inic10_value+"%";
            } else if (inic10_value >50 & inic10_value <80){
                var x = document.getElementById("bar_ini_4_4");
                x.className = "progress-bar bg-warning";
                x.style.width = inic10_value+"%";
            } else{
                var x = document.getElementById("bar_ini_4_4");
                x.className = "progress-bar bg-success";
                x.style.width = inic10_value+"%";
            }

            document.getElementById("value_4_5").innerHTML= inic11_value + "%";
            if(inic11_value <= 50){
                var x = document.getElementById("bar_ini_4_5");
                x.className = "progress-bar bg-danger";
                x.style.width = inic11_value+"%";
            } else if (inic11_value >50 & inic11_value <80){
                var x = document.getElementById("bar_ini_4_5");
                x.className = "progress-bar bg-warning";
                x.style.width = inic11_value+"%";
            } else{
                var x = document.getElementById("bar_ini_4_5");
                x.className = "progress-bar bg-success";
                x.style.width = inic11_value+"%";
            }

            document.getElementById("value_4_6").innerHTML= inic12_value + "%";
            if(inic12_value <= 50){
                var x = document.getElementById("bar_ini_4_6");
                x.className = "progress-bar bg-danger";
                x.style.width = inic12_value+"%";
            } else if (inic12_value >50 & inic12_value <80){
                var x = document.getElementById("bar_ini_4_6");
                x.className = "progress-bar bg-warning";
                x.style.width = inic12_value+"%";
            } else{
                var x = document.getElementById("bar_ini_4_6");
                x.className = "progress-bar bg-success";
                x.style.width = inic1_value+"%";
            }

            document.getElementById("value_4_7").innerHTML= inic13_value + "%";
            if(inic13_value <= 50){
                var x = document.getElementById("bar_ini_4_7");
                x.className = "progress-bar bg-danger";
                x.style.width = inic13_value+"%";
            } else if (inic13_value >50 & inic13_value <80){
                var x = document.getElementById("bar_ini_4_7");
                x.className = "progress-bar bg-warning";
                x.style.width = inic13_value+"%";
            } else{
                var x = document.getElementById("bar_ini_4_7");
                x.className = "progress-bar bg-success";
                x.style.width = inic13_value+"%";
            }

            document.getElementById("value_4_8").innerHTML= inic14_value + "%";
            if(inic14_value <= 50){
                var x = document.getElementById("bar_ini_4_8");
                x.className = "progress-bar bg-danger";
                x.style.width = inic14_value+"%";
            } else if (inic14_value >50 & inic14_value <80){
                var x = document.getElementById("bar_ini_4_8");
                x.className = "progress-bar bg-warning";
                x.style.width = inic14_value+"%";
            } else{
                var x = document.getElementById("bar_ini_4_8");
                x.className = "progress-bar bg-success";
                x.style.width = inic14_value+"%";
            }

            document.getElementById("value_4_9").innerHTML= inic15_value + "%";
            if(inic15_value <= 50){
                var x = document.getElementById("bar_ini_4_9");
                x.className = "progress-bar bg-danger";
                x.style.width = inic15_value+"%";
            } else if (inic15_value >50 & inic15_value <80){
                var x = document.getElementById("bar_ini_4_9");
                x.className = "progress-bar bg-warning";
                x.style.width = inic15_value+"%";
            } else{
                var x = document.getElementById("bar_ini_4_9");
                x.className = "progress-bar bg-success";
                x.style.width = inic15_value+"%";
            }

            document.getElementById("value_5_1").innerHTML= inic16_value + "%";
            if(inic16_value <= 50){
                var x = document.getElementById("bar_ini_5_1");
                x.className = "progress-bar bg-danger";
                x.style.width = inic16_value+"%";
            } else if (inic16_value >50 & inic16_value <80){
                var x = document.getElementById("bar_ini_5_1");
                x.className = "progress-bar bg-warning";
                x.style.width = inic16_value+"%";
            } else{
                var x = document.getElementById("bar_ini_5_1");
                x.className = "progress-bar bg-success";
                x.style.width = inic16_value+"%";
            }

            document.getElementById("value_6_1").innerHTML= inic17_value + "%";
            if(inic17_value <= 50){
                var x = document.getElementById("bar_ini_6_1");
                x.className = "progress-bar bg-danger";
                x.style.width = inic17_value+"%";
            } else if (inic17_value >50 & inic17_value <80){
                var x = document.getElementById("bar_ini_6_1");
                x.className = "progress-bar bg-warning";
                x.style.width = inic17_value+"%";
            } else{
                var x = document.getElementById("bar_ini_6_1");
                x.className = "progress-bar bg-success";
                x.style.width = inic17_value+"%";
            }

            document.getElementById("value_6_2").innerHTML= inic18_value + "%";
            if(inic18_value <= 50){
                var x = document.getElementById("bar_ini_6_2");
                x.className = "progress-bar bg-danger";
                x.style.width = inic18_value+"%";
            } else if (inic18_value >50 & inic18_value <80){
                var x = document.getElementById("bar_ini_6_2");
                x.className = "progress-bar bg-warning";
                x.style.width = inic18_value+"%";
            } else{
                var x = document.getElementById("bar_ini_6_2");
                x.className = "progress-bar bg-success";
                x.style.width = inic18_value+"%";
            }

            document.getElementById("value_7_1").innerHTML= inic19_value + "%";
            if(inic19_value <= 50){
                var x = document.getElementById("bar_ini_7_1");
                x.className = "progress-bar bg-danger";
                x.style.width = inic19_value+"%";
            } else if (inic19_value >50 & inic19_value <80){
                var x = document.getElementById("bar_ini_7_1");
                x.className = "progress-bar bg-warning";
                x.style.width = inic19_value+"%";
            } else{
                var x = document.getElementById("bar_ini_7_1");
                x.className = "progress-bar bg-success";
                x.style.width = inic19_value+"%";
            }
        },
        error: function(e){
            console.log(e);
        }
    });
});
$(document).ready(function(){
    var datamain;
    var databsc = [];

    $.ajax({
        type: 'GET',
        url:'/datajson',
        dataType: 'text',
        contentType:'charset=utf-8',
        success: function (response){
            
            var datos = JSON.parse(response);
            var obj1_value = parseInt(datos[1][1]);
            var obj2_value = parseInt(datos[2][1]);
            var obj3_value = parseInt(datos[3][1]);
            var obj4_value = parseInt(datos[4][1]);
            var obj5_value = parseInt(datos[5][1]);
            var obj6_value = parseInt(datos[6][1]);
            var obj7_value = parseInt(datos[7][1]);

            
            $.ajax({
                type: 'GET',
                url:'/data-bsc-json',
                dataType: 'text',
                contentType:'charset=utf-8',
                success: function (response_bsc){
                    
                    var datos_bsc = JSON.parse(response_bsc);
                    var obj1_bsc_value = parseInt(datos_bsc[1][1]);
                    var obj2_bsc_value = parseInt(datos_bsc[2][1]);
                    var obj3_bsc_value = parseInt(datos_bsc[3][1]);
                    var obj4_bsc_value = parseInt(datos_bsc[4][1]);
                    var obj5_bsc_value = parseInt(datos_bsc[5][1]);
                    var obj6_bsc_value = parseInt(datos_bsc[6][1]);
                    var obj7_bsc_value = parseInt(datos_bsc[7][1]);

                    // generate chart bar

                    /*
                    var marksCanvas = document.getElementById("marksChart");

                    Chart.defaults.global.defaultFontFamily = "Lato";
                    Chart.defaults.global.defaultFontSize = 18;

                    var marksData = {
                    labels: ["Obj 1", "Obj 2", "Obj 3", "Obj 4", "Obj 5", "Obj 6", "Obj 7"],
                    datasets: [{
                        label: "Balanced ScoreCard",
                        backgroundColor: "transparent",
                        borderColor: "rgba(200,0,0,0.6)",
                        fill: false,
                        radius: 6,
                        pointRadius: 6,
                        pointBorderWidth: 3,
                        pointBackgroundColor: "orange",
                        pointBorderColor: "rgba(200,0,0,0.6)",
                        pointHoverRadius: 10,
                        data: [obj1_bsc_value, obj2_bsc_value, obj3_bsc_value, obj4_bsc_value, obj5_bsc_value, obj6_bsc_value, obj7_bsc_value]
                    }, {
                        label: "Nuevo Sistema",
                        backgroundColor: "transparent",
                        borderColor: "rgba(0,0,200,0.6)",
                        fill: false,
                        radius: 6,
                        pointRadius: 6,
                        pointBorderWidth: 3,
                        pointBackgroundColor: "cornflowerblue",
                        pointBorderColor: "rgba(0,0,200,0.6)",
                        pointHoverRadius: 10,
                        data: [obj1_value, obj2_value, obj3_value, obj4_value, obj5_value, obj6_value, obj7_value]
                    }]
                    };

                    var chartOptions = {
                    scale: {
                        ticks: {
                        beginAtZero: true,
                        min: 0,
                        max: 100,
                        stepSize: 20
                        },
                        pointLabels: {
                        fontSize: 18
                        }
                    },
                    legend: {
                        position: 'left'
                    }
                    };

                    var radarChart = new Chart(marksCanvas, {
                    type: 'radar',
                    data: marksData,
                    options: chartOptions
                    });

                    */

                   function number_format(number, decimals, dec_point, thousands_sep) {
                    // *     example: number_format(1234.56, 2, ',', ' ');
                    // *     return: '1 234,56'
                    number = (number + '').replace(',', '').replace(' ', '');
                    var n = !isFinite(+number) ? 0 : +number,
                      prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
                      sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep,
                      dec = (typeof dec_point === 'undefined') ? '.' : dec_point,
                      s = '',
                      toFixedFix = function(n, prec) {
                        var k = Math.pow(10, prec);
                        return '' + Math.round(n * k) / k;
                      };
                    // Fix for IE parseFloat(0.55).toFixed(0) = 0;
                    s = (prec ? toFixedFix(n, prec) : '' + Math.round(n)).split('.');
                    if (s[0].length > 3) {
                      s[0] = s[0].replace(/\B(?=(?:\d{3})+(?!\d))/g, sep);
                    }
                    if ((s[1] || '').length < prec) {
                      s[1] = s[1] || '';
                      s[1] += new Array(prec - s[1].length + 1).join('0');
                    }
                    return s.join(dec);
                  }

                   var marksCanvas = document.getElementById("marksChart");

                   Chart.defaults.global.defaultFontFamily = "Lato";
                   Chart.defaults.global.defaultFontSize = 18;
                   
                   var marksData = {
                     labels: ["Obj 1", "Obj 2", "Obj 3", "Obj 4", "Obj 5", "Obj 6", "Obj 7"],
                     datasets: [{
                       label: "Balanced ScoreCard",
                       backgroundColor: "transparent",
                       borderColor: "rgba(200,0,0,0.6)",
                       fill: false,
                       radius: 6,
                       pointRadius: 6,
                       pointBorderWidth: 3,
                       pointBackgroundColor: "orange",
                       pointBorderColor: "rgba(200,0,0,0.6)",
                       pointHoverRadius: 10,
                       data: [obj1_bsc_value, obj2_bsc_value, obj3_bsc_value, obj4_bsc_value, obj5_bsc_value, obj6_bsc_value, obj7_bsc_value]
                     }, {
                       label: "Indicadores inteligentes",
                       backgroundColor: "transparent",
                       borderColor: "rgba(0,0,200,0.6)",
                       fill: false,
                       radius: 6,
                       pointRadius: 6,
                       pointBorderWidth: 3,
                       pointBackgroundColor: "cornflowerblue",
                       pointBorderColor: "rgba(0,0,200,0.6)",
                       pointHoverRadius: 10,
                       data: [obj1_value, obj2_value, obj3_value, obj4_value, obj5_value, obj6_value, obj7_value]
                     }]
                   };
                   
                   var chartOptions = {
                     scale: {
                       ticks: {
                         beginAtZero: true,
                         min: 0,
                         max: 100,
                         stepSize: 20
                       },
                       pointLabels: {
                         fontSize: 18
                       }
                     },
                     legend: {
                       position: 'left'
                     },
                     yAxes: [{
                        ticks: {
                          min: 0,
                          max: 100,
                          maxTicksLimit: 10,
                          padding: 10,
                          // Include a porcent sign in the ticks
                          callback: function(value, index, values) {
                            return  number_format(value) + '%';
                          }
                        },
                        gridLines: {
                          color: "rgb(234, 236, 244)",
                          zeroLineColor: "rgb(234, 236, 244)",
                          drawBorder: false,
                          borderDash: [2],
                          zeroLineBorderDash: [2]
                        }
                      }],
                      tooltips: {
                        titleMarginBottom: 10,
                        titleFontColor: '#6e707e',
                        titleFontSize: 14,
                        backgroundColor: "rgb(255,255,255)",
                        bodyFontColor: "#858796",
                        borderColor: '#dddfeb',
                        borderWidth: 1,
                        xPadding: 15,
                        yPadding: 15,
                        displayColors: false,
                        caretPadding: 10,
                        callbacks: {
                          label: function(tooltipItem, chart) {
                            var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
                            return datasetLabel + ': ' + number_format(tooltipItem.yLabel) + ' %';
                          }
                        }
                      },
                      
                   };
                   
                   var radarChart = new Chart(marksCanvas, {
                     type: 'radar',
                     data: marksData,
                     options: chartOptions
                   });
                                
                },
                error: function(e){
                    console.log(e);
                }
            });
          
        },
        error: function(e){
            console.log(e);
        },

    });

    
});
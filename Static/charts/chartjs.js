   $(window).on('load', function () {
        
        var analytics_chart_data = JSON.parse($(`#analytics_chart_data`).html())
 
        var chartWrapper = $('.chartjs')
        var    flatPicker = $('.flat-picker')
        var    lineChartEx = $('.line-chart-ex')
        var    serviceAnalyticsChart = $('.service_analytics_chart')
        // Color Variables
        var primaryColorShade = '#836AF9',
            yellowColor = '#ffe800',
            successColorShade = '#28dac6',
            warningColorShade = '#ffe802',
            warningLightColor = '#FDAC34',
            infoColorShade = '#299AFF',
            greyColor = '#4F5D70',
            blueColor = '#2c9aff',
            blueLightColor = '#84D0FF',
            greyLightColor = '#EDF1F4',
            tooltipShadow = 'rgba(0, 0, 0, 0.25)',
            lineChartPrimary = '#666ee8',
            lineChartDanger = '#ff4961',
            labelColor = '#6e6b7b',
            grid_line_color = 'rgba(200, 200, 200, 0.2)'; // RGBA color helps in dark layout
            


         
            // Detect Dark Layout
            if ($('html').hasClass('dark-layout')) {
                labelColor = '#b4b7bd';
            }

        // Wrap charts with div of height according to their data-height
        if (chartWrapper.length) {
            chartWrapper.each(function () {
                $(this).wrap($('<div style="height:' + this.getAttribute('data-height') +
                'px"></div>'));
            });
        }

        // Init flatpicker
        if (flatPicker.length) {
            var date = new Date();
            flatPicker.each(function () {
                $(this).flatpickr({
                    mode: 'range',
                    defaultDate: ['2019-05-01', '2019-05-10']
                });
            });
        }




 
        // Service Analytics Chart
        // --------------------------------------------------------------------
        if (serviceAnalyticsChart.length) { 
            var lineChartElement = new Chart(serviceAnalyticsChart, {
                type: 'line',
                plugins: [
                    // to add spacing between legends and chart
                    {
                        beforeInit: function (chart) {
                            chart.legend.afterFit = function () {
                                this.height += 20;
                            };
                        }
                    }
                ],
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    backgroundColor: false,
                    hover: {
                        mode: 'label'
                    },
                    tooltips: {
                        // Updated default tooltip UI 
                        // cornerRadius: 0,
                        shadowOffsetX: 1,
                        shadowOffsetY: 1,
                        shadowBlur: 8,
                        shadowColor: tooltipShadow,
                        backgroundColor: window.colors.solid.white,
                        titleFontColor: window.colors.solid.black,
                        bodyFontColor: window.colors.solid.black,
                        // callbacks: {
                        //     title: function(t, d) { 
                        //         var tooltip_index = t[0].index ;
                        //         var tooltip_default_text = "Date = "+d.labels[tooltip_index] ;
                        //         var custom_tooltip_text = d.tooltips[tooltip_index] ;
                        //         if (!custom_tooltip_text){
                        //             custom_tooltip_text = []
                        //         }
                        //         console.log("custom_tooltip_text = ",custom_tooltip_text)
                        //         custom_tooltip_text = custom_tooltip_text.join("\n") + "\n" + tooltip_default_text
                        //        return `${custom_tooltip_text}` ;
                        //     }
                        //  }

                    },
                    layout: {
                        padding: {
                            top: -15,
                            bottom: -25,
                            left: -15
                        }
                    },
                    scales: {
                        xAxes: [{
                            display: true,
                            scaleLabel: {
                                display: true
                            },
                            gridLines: {
                                display: true,
                                color: grid_line_color,
                                zeroLineColor: grid_line_color
                            },
                            ticks: {
                                fontColor: labelColor,
                                callback: function(t) { 
                                    return t
                                }

                            }
                        }],
                        yAxes: [{
                            display: true,
                            scaleLabel: {
                                display: true
                            },
                            ticks: {
                                // stepSize: 100,
                                // min: 0,
                                // max: 4000,
                                fontColor: labelColor
                            },
                            gridLines: {
                                display: true,
                                color: grid_line_color,
                                zeroLineColor: grid_line_color
                            }
                        }]
                    },
                    legend: {
                        position: 'top',
                        align: 'start',
                        labels: {
                            usePointStyle: true,
                            padding: 25,
                            boxWidth: 9
                        }
                    }
                },
                data: { 
                    labels: analytics_chart_data.labels,
                    datasets: [{
                            data: analytics_chart_data.data,
                            // data: [],
                            label: 'Payments',
                            borderColor: lineChartPrimary,
                            lineTension: 0.2,
                            pointStyle: 'circle',
                            backgroundColor: lineChartPrimary,
                            fill: false,
                            pointRadius: 5,
                            pointHoverRadius: 5,
                            pointHoverBorderWidth: 5,
                            pointBorderColor: 'transparent',
                            pointHoverBorderColor: window.colors.solid.white,
                            pointHoverBackgroundColor: lineChartPrimary,
                            pointShadowOffsetX: 1,
                            pointShadowOffsetY: 1,
                            pointShadowBlur: 5,
                            pointShadowColor: tooltipShadow
                        },
                        // {
                        //     data: [80, 125, 105, 130, 215, 195, 140, 160, 230, 300, 220, 170, 210,
                        //         200, 280
                        //     ],
                        //     label: 'Asia',
                        //     borderColor: lineChartPrimary,
                        //     lineTension: 0.2,
                        //     pointStyle: 'circle',
                        //     backgroundColor: lineChartPrimary,
                        //     fill: false,
                        //     pointRadius: 1,
                        //     pointHoverRadius: 5,
                        //     pointHoverBorderWidth: 5,
                        //     pointBorderColor: 'transparent',
                        //     pointHoverBorderColor: window.colors.solid.white,
                        //     pointHoverBackgroundColor: lineChartPrimary,
                        //     pointShadowOffsetX: 1,
                        //     pointShadowOffsetY: 1,
                        //     pointShadowBlur: 5,
                        //     pointShadowColor: tooltipShadow
                        // },
                        // {
                        //     data: [80, 99, 82, 90, 115, 115, 74, 75, 130, 155, 125, 90, 140, 130,  180    ],
                        //     label: 'Africa',
                        //     borderColor: warningColorShade,
                        //     lineTension: 0.2,
                        //     pointStyle: 'circle',
                        //     backgroundColor: warningColorShade,
                        //     fill: false,
                        //     pointRadius: 3,
                        //     pointHoverRadius: 5,
                        //     pointHoverBorderWidth: 5,
                        //     pointBorderColor: 'transparent',
                        //     pointHoverBorderColor: window.colors.solid.white,
                        //     pointHoverBackgroundColor: warningColorShade,
                        //     pointShadowOffsetX: 1,
                        //     pointShadowOffsetY: 1,
                        //     pointShadowBlur: 5,
                        //     pointShadowColor: tooltipShadow
                        // }
                    ]
                }
            });

 

        }


    });

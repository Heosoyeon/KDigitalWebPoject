/*!
* Start Bootstrap - Modern Business v5.0.5 (https://startbootstrap.com/template-overviews/modern-business)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-modern-business/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
function displayChart(data){
    const chart = Highcharts.chart('container', {
        title: {
            text: '별점 분포'
        },
        subtitle: {
            text: '별점'
        },
        xAxis: {
            categories: ['1', '2', '3', '4', '5']
        },
        series: data
    });
};
function getdata(){
    $.ajax({
        url:'/item/chart',
        success:function(data){
            displayChart(data)
        }
    })
};

$(document).ready(function(){
    getdata();
});
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<link href="/FlatUI/dist/css/vendor/bootstrap.min.css" rel="stylesheet">
	<link href="/FlatUI/dist/css/flat-ui.css" rel="stylesheet">
	<link href="/FlatUI/docs/assets/css/demo.css" rel="stylesheet">
	<link rel="shortcut icon" href="FlatUI/img/favicon.ico">
</head>
<body>
	<div id="container" style="min-width:400px;height:400px"></div>
	<script src="/FlatUI/dist/js/vendor/jquery.min.js"></script>
	<script src="http://cdn.hcharts.cn/highcharts/highcharts.js"></script>
	<script  type="text/javascript" charset="UTF-8">
	$(function () {
    $('#container').highcharts({
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Results of Movie Recommended Collective Algorithm'
        },
        subtitle: {
            text: 'By: Chen Di'
        },
        xAxis: {
            categories: {{!movie}},
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Score ',
                align: 'high'
            },
            labels: {
                overflow: 'justify'
            }
        },
        tooltip: {
            valueSuffix: ' Scores'
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true
                }
            }
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'top',
            x: -40,
            y: 100,
            floating: true,
            borderWidth: 1,
            backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
            shadow: true
        },
        credits: {
            enabled: false
        },
        series: [{
            name: '',
            data: {{!score}}
        }]
    });
});</script>
</body>
</html>

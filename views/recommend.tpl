<<html>
<head>
	<title>Recommend</title>
</head>
<body>

</body>
</html>
<p>结果出来啦！向你推荐的影片排序是</p>
%for row in rank:
	<p>{{row[1]}}     综合评分为:{{row[0]}}</p>

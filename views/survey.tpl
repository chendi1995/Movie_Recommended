<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<link href="FlatUI/dist/css/vendor/bootstrap.min.css" rel="stylesheet">
	<link href="FlatUI/dist/css/flat-ui.css" rel="stylesheet">
	<link href="FlatUI/docs/assets/css/demo.css" rel="stylesheet">
	<link rel="shortcut icon" href="FlatUI/img/favicon.ico">
</head>
<body>
	<div class="span12">
		<div class="demo-type-example">
	      		<h3><img src="FlatUI/img/icons/svg/clipboard.svg" alt="Clipboard">请务必诚实地给下列影片评分，这会影响给您推荐地准确性</h3>
      		</div>
		<div class="alert alert-info">
			<button type="button" class="close" data-dismiss="alert">×</button>
			<p>
				提示：未看过的影片不评分
			</p>
		</div>

		<form class="form-inline" method="POST">
			<fieldset>
				<table class="table">
					<tbody>
						%for i in range(10):
						<tr>
							%for j in range(10):
							<td>
								<a href="{{movielist[10*i+j][1]}}">
								<img src="{{movielist[10*i+j][2]}}" width="96" height="128">
								<p>{{movielist[10*i+j][0]}}</p>
								</a>
								<p> </p>
								<input type="text" style="width:64px; height:32px;" class="form-control" id="{{movielist[10*i+j][0]}}" name="{{10*i+j}}"  maxlength="3">
							</td>
							%end
						</tr>
						%end
					</tbody>
				</table>

				<button class="btn btn-primary btn-lg btn-block" type="input" href="#">提交</button>
			</fieldset>
		</form>
	</div>
	<script src="FlatUI/dist/js/vendor/jquery.min.js"></script>
	<script src="FlatUI/dist/js/vendor/video.js"></script>
	<script src="FlatUI/dist/js/flat-ui.min.js"></script>
	<script src="FlatUI/docs/assets/js/application.js"></script>
	 <script src="FlatUI/js/stickUp.min.js"></script>
	<script src="//code.jquery.com/jquery-1.11.3.min.js"></script>
	<script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>

	<script>videojs.options.flash.swf = "FlatUI/dist/js/vendors/video-js.swf"</script>
	<script type="text/javascript">
              //initiating jQuery
              jQuery(function($) {
                $(document).ready( function() {
                  //enabling stickUp on the '.navbar-wrapper' class
                  $(alert alert-info).stickUp();
                });
              });

            </script>
</body>
</html>

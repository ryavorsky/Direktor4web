<?php

	header('Content-Type: text/html; charset=utf-8');
	echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />';
	echo "<style type='text/css'>
		body{
		background:#BBFFBB;
		color: #113F00;
		font-family:'Lucida Console',sans-serif !important;
		font-size: 16px;
		}
		</style>";

	echo "<body>";
	echo "<a href=\"index.html\">Вернуться на главную страницу</a><br/><br/>";

	echo "<br />Статус обработки:<br /><hr/><pre><code>";
	$res = file_get_contents('upload/status.txt');
	echo $res;  
	echo "</code></pre></body>"; 

?>
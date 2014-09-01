<?php

	header('Content-Type: text/html; charset=utf-8');
	echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />';

	echo "<body>";
	echo "<a href=\"index.html\">Вернуться на главную страницу</a><br/><br/>";

	echo "<br />Готовые отчёты:<br /><hr/><pre><code>";
	$dirlist = scandir('/home/u415348/socio2014.obrkvartal.ru/www/reports/')
	$res = file_get_contents('upload/status.txt');
	echo $dirlist;  
	echo "</code></pre></body>"; 

?>
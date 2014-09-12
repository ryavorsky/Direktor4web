<?php

	header('Content-Type: text/html; charset=utf-8');
	echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />';

	echo "<body>";
	echo "<a href=\"index.html\">Вернуться на главную страницу</a><br/><br/>";

	echo "<br />Готовые отчёты:<br /><hr/><pre><code>";
	$dirList = scandir('/home/u415348/socio2014.obrkvartal.ru/www/reports/');
	$res = "<br/>";
	foreach ($dirList as $value) {
		if (strlen($value) > 3) {
			$link = '<a href="reports/'.$value.'/Report_template.html"  target="_newtab">'.$value.'</a>';
			echo $link."\n"  ;
		} ;
	} ;

	echo "</code></pre></body>"; 

?>
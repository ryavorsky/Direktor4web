<?php

	header('Content-Type: text/html; charset=utf-8');
	echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />';

	$timestamp = date('Y-m-d-H-i-s');
	
	$dirname = $_GET['name'];
	
	$success0 = mkdir('todo/'.$dirname);
	$success0 = $success0.'<br />'.mkdir('todo/'.$dirname.'/svg');
	$success0 = $success0.'<br />'.mkdir('todo/'.$dirname.'/png');
	$success1 = '';
	$names = array('pie211',	'pie212a',	'pie212b',	'pie212c',	'pie212d',	'pie213a',	'pie213b',	'pie213c',	'pie213d',	'pie213e',	'pie214a',	'pie214b',	'pie214c',	'pie214d',	'pie214e',	'pie221',	'pie222a',	'pie222b',	'pie222c',	'pie222d',	'pie223a',	'pie223b',	'pie223c',	'pie223d',	'pie223e',	'pie224a',	'pie224b',	'pie224c',	'pie224d',	'pie225',	'pie231',	'pie232',	'pie233',	'pie234',	'pie311',	'pie312a',	'pie312b',	'pie312c',	'pie312d',	'pie313a',	'pie313b',	'pie313c',	'pie313d',	'pie313e',	'pie321',	'pie322a',	'pie322b',	'pie322c',	'pie322d',	'pie323a',	'pie323b',	'pie323c',	'pie323d',	'pie323e',	'pie324a',	'pie324b',	'pie324c',	'pie41',	'pie421',	'pie422',	'pie423',	'pie51',	'pie52a',	'pie52b',	'pie52c',	'pie52d',	'pie53a',	'pie53b',	'pie53c',	'pie53d',	'pie53e',	'pie54a',	'pie54b',	'pie_no',	'pie_yes');
	foreach ($names as $pic_name) {
		$source_file_name = 'http://socio2014.obrkvartal.ru/reports/'.$dirname.'/'.$pic_name.'.svg';
		$res_file_name = 'todo/'.$dirname.'/svg/'.$pic_name.'.svg';
		$success1 = $success1.'<br />'.copy('http://socio2014.obrkvartal.ru/reports/Res_export_8.txt_2014-10-9_22h0m1s/pie212b.svg',$res_file_name);
	}


	

	echo '<body><br />Timestamp: '.$timestamp.'<br /><br />Dir: '.$dirname ;
	echo '<br />Source: '.$source_file_name;
	echo '<br />Dest: '.$res_file_name;
	echo '<br />mkdir result: '.$success0;
	echo '<br />Copy result: '.$success1;
	echo '</body>'; 
	
	$status_file_name = 'todo/call'.$timestamp.'.txt';
	$status_file = fopen($status_file_name, 'w');
	fwrite($status_file, "When: ".date('Y-m-d H:i:s'). PHP_EOL);
	fclose($status_file);
	

	//exec('/usr/bin/node /home/virtwww/w_rost_8baa4f5f/http/convert/hello.js');
	//file_put_contents("Tmpfile.svg", file_get_contents("http://socio2014.obrkvartal.ru/reports/".$dirname."/pie212b.svg"));
	
?>
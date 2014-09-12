<?php
$allowedExts = array("txt");
$temp = explode(".", $_FILES["file"]["name"]);
$extension = end($temp);

if (($_FILES["file"]["type"] == "text/plain")
&& ($_FILES["file"]["size"] < 200000)
&& in_array($extension, $allowedExts)) {
  if ($_FILES["file"]["error"] > 0) {
    echo "Return Code: " . $_FILES["file"]["error"] . "<br>";
  } else {
  
    echo "Upload: " . $_FILES["file"]["name"] . "<br>";
    echo "Type: " . $_FILES["file"]["type"] . "<br>";
    echo "Size: " . ($_FILES["file"]["size"] / 1024) . " kB<br>";
    echo "Temp file: " . $_FILES["file"]["tmp_name"] . "<br>";

    if (file_exists("upload/" . $_FILES["file"]["name"])) {
      echo $_FILES["file"]["name"] . " already exists. ";
    } else {

      move_uploaded_file($_FILES["file"]["tmp_name"],
      "upload/" . $_FILES["file"]["name"]);
      echo "Stored: " . "upload/" . $_FILES["file"]["name"];
    
      $old_status = file_get_contents('upload/status.txt');
      $f = fopen('upload/status.txt', 'w');
      fwrite($f, "When: ".date('Y-m-d H:i:s'). PHP_EOL);
      fwrite($f, "What: New file uploaded". PHP_EOL);
      fwrite($f, "Name: upload/" .$_FILES["file"]["name"]. PHP_EOL);
      fwrite($f, "Type: " . $_FILES["file"]["type"]. ". Size: " . ($_FILES["file"]["size"] / 1024) . " kB". PHP_EOL. PHP_EOL);
      fwrite($f, $old_status);
      fclose($f);
      
      //$old_todo_list = file_get_contents('todo.txt');
      $f_todo = fopen('todo.txt', 'a');
      fwrite($f_todo, '/home/u415348/socio2014.obrkvartal.ru/www/upload/'.$_FILES["file"]["name"]."\n"); 
      //fwrite($f_todo, $old_status);
      fclose($f_todo);
    }
  }
} else {
  echo "Invalid file";
}

echo "<br/><br/><br/><a href=\"index.html\">Return to the main page</a>";
echo "<br/><br/><br/><a href=\"script1.php\">Check the status</a>";


?>
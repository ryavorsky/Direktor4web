<?php
$allowedExts = array("gif", "jpeg", "jpg", "png", "txt");
$temp = explode(".", $_FILES["file"]["name"]);
$extension = end($temp);

if ((($_FILES["file"]["type"] == "image/gif")
|| ($_FILES["file"]["type"] == "image/jpeg")
|| ($_FILES["file"]["type"] == "image/jpg")
|| ($_FILES["file"]["type"] == "image/pjpeg")
|| ($_FILES["file"]["type"] == "image/x-png")
|| ($_FILES["file"]["type"] == "text/plain")
|| ($_FILES["file"]["type"] == "image/png"))
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
	  
	  $old = file_get_contents('upload/status.txt');
      $f = fopen('upload/status.txt', 'w');
      fwrite($f, "When: ".date('Y-m-d H:i:s'));
      fwrite($f, "<br/>New file stored in: upload/" .$_FILES["file"]["name"]);
      fwrite($f, ". Type: " . $_FILES["file"]["type"]);
      fwrite($f, ". Size: " . ($_FILES["file"]["size"] / 1024) . " kB<br/><br/>");
      fwrite($f, $old);
      fclose($f);

    }
  }
} else {
  echo "Invalid file";
}

echo "<br/><br/><br/><a href=\"index.html\">Return to the main page</a>";


?>
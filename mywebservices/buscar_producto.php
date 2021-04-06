<?php

include 'conexion.php';
$island=$_GET['island'];

$query = "select * from eventos where ISLA = '$island'";
$result = $connection -> query($query);

while($row=$result -> fetch_array()){
	$product[] = array_map('utf8_encode', $row);
}

echo json_encode($product);
$result -> close();

?>
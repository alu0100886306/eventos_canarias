<?php

include 'conexion.php';

if (isset($_GET["id"])){
	$id=$_GET['id'];
	$query = "UPDATE eventos SET N_CLICKS = N_CLICKS + 1 WHERE MAS_INFO = '$id'";
	$result = $connection -> query($query);
	// $result -> close();
	$product = array();
	$product[] = $result;

	echo json_encode($product);
}

?>
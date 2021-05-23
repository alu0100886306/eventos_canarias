<?php

include 'conexion.php';

$cond = array();
$query = "select DATE_FORMAT(FECHA_INICIO,'%d-%m-%Y'),
DATE_FORMAT(FECHA_FIN,'%d-%m-%Y'),
DURACION_DIAS,
TIPO_EVENTO,
ISLA,
MUNICIPIO,
DENOMINACION_ESPACIO,
LUGAR,
TITULO,
DESCRIPCION,
HORA,
MINUTO,
MAS_INFO,
URL_IMAGEN from eventos ORDER BY `N_CLICKS` DESC LIMIT 6";

$result = $connection -> query($query);

$product = array();

while($row=$result -> fetch_array()){
	$product[] = array_map('utf8_encode', $row);
}

echo json_encode($product);
$result -> close();

?>
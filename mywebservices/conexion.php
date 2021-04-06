<?php

$hostname='localhost';
$database='testing';
$username='root';
$password='admin';

$connection=new mysqli($hostname,$username,$password,$database);
if($connection->connect_errno){
	echo "Lo sentimos, el sitio web está experimentando problemas";
}

?>
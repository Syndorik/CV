<?php	
	$serveur = 'localhost';
	$admin = 'id3291796_syndorik';
	$pass = 'hkl0c48zrt';
	$bd = "id3291796_personnes";
	$dsn = 'mysql:host='.$serveur.';dbname='.$bd;
	$pdo = new PDO($dsn,$admin,$pass) or die("erreur");
?>
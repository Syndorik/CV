<!doctype html>
<html lang="fr">
<head>
	<meta charset="utf-8">
	<title> Affichage des données </title>
</head>
	<body>
		<?php
		include_once("/storage/ssd4/796/3291796/public_html/donnees.inc.php");
		 $add = 0;
		 $nom = $_POST['nom'];
		 $prenom = $_POST['prenom'];
		 $pseudo = $_POST['pseudo'];
		 $email = $_POST['email'];
		 $pass = $_POST['pwd'];
		 $bat = $_POST['bat'];
		 if ($bat == "autre") {
		 	$add = $_POST['addr'];
		 }
		 else{
		 	$add = $bat." ".$_POST['nch'];
		 }

		 $req = "INSERT INTO `id3291796_personnes`.`Users`(
		 				`user_ID`,`username`, `last_name`, `first_name`, `email`, `password`, `address`,`tokens`,`mark`)
		 		VALUES(
		 			NULL,'".$pseudo."','".$nom."','".$prenom."','".$email."','".$pass."','".$add."','10','0'
		 		)

		 ";	
		 $res = $pdo->query($req);
         echo "Hi <BR>" ;
       ?>
		
		</section>

	</body>
</html>



<!DOCTYPE html>
<html>
<head>
	<title>Inscription</title>
</head>
<body>
<form action="/Accueil/resultat-formulaire.php" method="post" id="mf">
	<div id = "Sexe">
		<label for= "Sexe">Sexe : </label>
		<input type="radio" name="Sexe" id= "Sexe1" value ="Homme"> Homme
		<input type="radio" name="Sexe" id= "Sexe2" value ="Femme"> Femme
		<span ></span> <br>

	</div>
	<div>
		<label for= "Nom">Nom : </label>
		<input type="text" name="text" id= "Nom">
		<span></span>
	</div>
	<div>
		<label for="Prenom">Prénom : </label>
		<input type="text" name="text" id = "Prenom">
		<span></span>
	</div>
	<div>
		<label for="Pseudo">Pseudo : </label>
		<input type="text" name="Pseudo" id = "Pseudo">
		<span></span>
	</div>
	<div>
		<label for="Age">Age : </label>
		<input type ="text" name= "text" id ="Age">
		<span></span>
	</div>
	<div>
		<label for="Mot de passe">Mot de passe : </label>
		<input type="password" name="pass" id = "pass">
		<span></span>
	</div>
	<div>
		<label for="Mot de passe conf">Mot de passe (confirmation): </label>
		<input type="password" name="pass1" id = "pass1">
		<span></span>
	</div>
	<div id="ctry">
		<label for="Country">Pays : </label>
		<select>
			<option value= "France">France</option>
			<option value= "Espagne"> Espagne</option>
		</select>
		<span></span>
	</div>
	<div>
		<label for= "Conf">J'accepte de recevoir du spam</label>
		<input type="checkbox" name="ck" id= "ck">
		<span></span>
	</div>
	<div class="button">
        <button type="submit" id = 'btn'>Envoyer votre message</button>
    </div>
</form>
<script src = "javascript/form.js"></script>
</body>
</html>
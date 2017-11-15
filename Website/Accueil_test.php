    <!DOCTYPE html>
    <html lang="fr">
      <head>
        <title>Inscription</title>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="style.css" />
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
        <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
          <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
          <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
        <![endif]-->
        </head>
    <body>
        <div class="container">
            <div class="row" id="first-row">
                <div class="col-md-12" id="panel-parent">
                    <div class="panel panel-default " >
                        <div class="panel-heading">
                            <div class="panel-title text-center">Inscription</div>
                        </div>
                        <div class="panel-body">
                            <div class="col-md-6 " id="logo_col">
                                <p id="logo_p"><img class="img-responsive" id="logo" src="images/logo1_micro.png" alt="logo" height="80%" ></p>
                            </div>

                            <div class="col-md-6">
                                <form action="/Accueil/resultat-formulaire.php" method="post" id="mff">
                                    <div class="col-md-12" id = "mf">
                                        <div class="input-group">
                                            <span class="input-group-addon"><i class="glyphicon glyphicon-user"></i></span>
                                            <input class="form-control" type="text" name="prenom" id="Prenom" placeholder="Prénom" />
                                        </div>
                                        <span id="firstNameMsg" class = "span-warning"></span>

                                        <div class="input-group">
                                            <span class="input-group-addon"><i class="glyphicon glyphicon-user"></i></span>
                                            <input class="form-control" type="text" name="nom" id = "Nom" placeholder="Nom" />
                                        </div>
                                        <span id="lastNameMsg" class = "span-warning"></span>

                                        <div class="input-group">
                                            <span class="input-group-addon"><i class="glyphicon glyphicon-user"></i></span>
                                            <input class="form-control" type="text" name="pseudo" id = "Pseudo" placeholder="Pseudo" />
                                        </div>
                                        <span id="pseudoMsg" class = "span-warning"></span>

                                        <div class="input-group">
                                            <span class="input-group-addon"><i class="glyphicon glyphicon-envelope"></i></span>
                                            <input class="form-control" type="text" name="email" id="email" placeholder="Email" />
                                        </div>
                                        <span id="emailMsg" class = "span-warning"></span>
                                        
                                        <div class="input-group">
                                            <span class="input-group-addon"><i class="glyphicon glyphicon-lock"></i></span>
                                            <input class="form-control" type="password" name="pwd" id ="pass" placeholder="Mot de passe" />
                                        </div>
                                        <span id="passMsg" class = "span-warning"></span>

                                        <div class="input-group">

                                            <span class="input-group-addon"><i class="glyphicon glyphicon-lock"></i></span>
                                            <input class="form-control" type="password" name="pwd2" id = "pass1" placeholder="Vérification mot de passe" />
                                        </div>
                                        <span id="pass1Msg" class = "span-warning"></span>

                                        <div class="input-group" id="batt">
                                            <select class="form-control" id ="batiment" name ="bat">
                                                <option value= "null">Batiment</option>
                                                <option value= "i1">i1</option>
                                                <option value= "i2">i2</option>
                                                <option value= "i3">i3</option>
                                                <option value= "i4">i4</option>
                                                <option value= "i5">i5</option>
                                                <option value= "i6">i6</option>
                                                <option value= "i7">i7</option>
                                                <option value= "i8">i8</option>
                                                <option value= "i9">i9</option>
                                                <option value= "i10">i10</option>
                                                <option value= "i11">i11</option>
                                                <option value= "i12">i12</option>
                                                <option value = "autre">Autre</option>
                                            </select>
                                        </div>
                                        <span id="batMsg" class = "span-warning"></span>


                                        <div class="input-group" id = "yolo">
                                            <span class="input-group-addon"><i class="glyphicon glyphicon-home"></i></span>
                                            <input class="form-control" type="text" name="pseudo" id = "chambre" placeholder="Numéro de chambre (facultatif)" />
                                        </div> <!-- end input -->
                                        <span id="spanchbr" class = "span-warning"></span>


                                        <span id="sbm"></span>

                                        <div class="form-group button">
                                            <div class="col-md-12 controls">
                                                 <button type="submit" href="#" class="btn btn-primary pull-right"><i class="glyphicon glyphicon-log-in"></i> S'inscrire</button>
                                            </div>
                                        </div>
                                    </div>
                                </form>

                            </div>

                        </div>
                    </div>

                </div>
            </div>


            </div>
        </div>

        <script src = "javascript/form.js"></script>

  </body>
</html>

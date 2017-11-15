<!DOCTYPE html>
<html lang="fr">
  <head>
    <title>Mon compte</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
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
        <div class="container-fluid">
            <h1 class="text-center">Mon compte</h1>
            <div class="row well" id="info-row">
                <h2>Infos</h2>
                <div class="col-md-2">
                    <h4>Mes données</h4>
                    <ul>
                        <li>Pseudo : </li>
                        <li>Prénom :</li>
                        <li>Nom :</li>
                        <li>Mail :</li>
                        <li>Batiment :</li>
                        <li>Chambre :</li>
                    </ul>
                </div>
                <div class="col-md-2">
                    <h4>Jetons</h4>
                </div>

                <div class="col-md-2">
                    <h4>Ma note</h4>
                </div>
                <div class="col-md-3">
                    <h4>Mes titres</h4>
                </div>
                <div class="col-md-3">
                    <h4>Plus qu'à</h4>
                    <p><ul>
                        <li>Preter x objets avant de devenir ?</li>
                        <li>Emprunter x objets avant de devenir ?</li>
                        <li>Parrainer x personnes avant de devenir gourou !</li>
                    </ul></p>
                </div>
            </div>
            <div class="row well" id="objects-row">
                <h2>Objets</h2>
                <div class="col-md-4">
                    <h4>Mes objets</h4>
                    <p>Allez les chercher dans la base
                    <ul>
                        <li>Appareil à raclette</li>
                        <li>Casserole</li>
                    </ul></p>
                    <form action="index.html" method="post">
                        <div class="input-group button-group">

                            <input class="form-control" type="text" name="Object" placeholder="Nouvel objet à prêter" aria-describedby="plus-button">
                            <span id="plus-button" class="input-group-btn"><button class="btn btn-default form-control" type="button" name="button"><i class="glyphicon glyphicon-plus"></i></button></span>                            
                        </div>
                    </form>
                </div>
                <div class="col-md-4">
                    <h4>Objets que je prête</h4>
                    <p>Allez les chercher dans la base
                    <ul>
                        <li>Appareil à raclette à Alex</li>
                        <li>CAsserole à PH</li>
                    </ul></p>
                </div>
                <div class="col-md-4">
                    <h4>Objets que j'emprunte</h4>
                    <p>Aller les chercher dans la base
                    <ul>
                        <li>Surf de Paulo</li>
                        <li>Planche à repasser de JB</li>
                        <li>Afficher preteur et date ?</li>
                    </ul></p>
                </div>
            </div>
            <div class="row well" id="review-row">
                <h2>Mes reviews</h2>
                <p>Prête ou emprunte des objets pour recevoir des commentaires ;)</p>
            </div>
        </div>
    </body>

</html>

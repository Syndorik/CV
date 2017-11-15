
var nom = document.getElementById('Nom');
var prenom = document.getElementById('Prenom');
var pseudo = document.getElementById('Pseudo');
var email = document.getElementById('email');
var pass = document.getElementById('pass');
var passconf = document.getElementById('pass1');

var batiment = document.getElementById('batiment');
var chambre = document.getElementById('chambre');
var divchambre = document.getElementById('yolo');
var sbm = document.getElementById('sbm');
var mf = document.getElementById('mf');
var mff = document.getElementById('mff');


function verifLastName(name,ev){
	if(name.value.length>1){
		document.getElementById("lastNameMsg").innerHTML  = "";
	}
	else{
		warning = "Il doit y avoir au moins 2 caractères";
		document.getElementById("lastNameMsg").innerHTML = warning;
		ev.preventDefault();
	}
}

function verifFirstName(name,ev){
	if(name.value.length>1){
		document.getElementById("firstNameMsg").innerHTML = "";
	}
	else{
		warning = "Il doit y avoir au moins 2 caractères";
		document.getElementById("firstNameMsg").innerHTML = warning;
		ev.preventDefault();
	}
}

function verifadd(name,ev){
	if(name.value.length>3){
		document.getElementById("spip").innerHTML  = "";

	}
	else{
		warning = "Veuillez rentrer une adresse correcte";
		document.getElementById("spip").innerHTML = warning;
		ev.preventDefault();
	}
}


function verifpseudo(pseudo,ev){
	if(pseudo.value.length>6){
		document.getElementById("pseudoMsg").innerHTML  = "";

	}
	else{
		warning = "Il doit y avoir au moins 6 caractères";
		document.getElementById("pseudoMsg").innerHTML = warning;
		ev.preventDefault();
	}
}


function verifpass(pass1,pass2,ev){

	if(pass1.value === pass2.value && pass1.value.length>8){
		document.getElementById("passMsg").innerHTML  = "";
		document.getElementById("pass1Msg").innerHTML  = "";
	}
	else if(pass1.value !== pass2.value){
		warning = "Les mots de passe doivent correspondre";
		document.getElementById("pass1Msg").innerHTML  = warning;
		ev.preventDefault();
	}
	else if (pass1.value === pass2.value && pass1.value.length< 8){
		warning = "Le mot de passe doit contenir au moins 7 caractères";
		document.getElementById("pass1Msg").innerHTML  = warning;
		ev.preventDefault();
	}
}

function existin(txt,letter){
	txt1 = txt.value.split('');
	b = 0;
	for(var i =0; i< txt1.length; i++){
		if(txt1[i] === letter){
			b =1;
		}
	}
	return b;
}

function verifmail(mail,ev){
	if(existin(mail,"@")){
		document.getElementById("emailMsg").innerHTML  = "";
	}
	else{
		warning = "Veuillez rentrer une adresse mail correct";
		document.getElementById("emailMsg").innerHTML  = warning;
		ev.preventDefault();
	}
}

function verifbat(batiment,ev){
	dvch = document.getElementById('yolo');
	spchbr = document.getElementById('spanchbr');
	if(batiment.value == "null"){
		warning = "Veuillez sélectionner votre bâtiment";
		document.getElementById("batMsg").innerHTML  = warning;
		ev.preventDefault();
	}
	else if(batiment.value == "autre"){
		dvch.parentNode.removeChild(dvch);
		spchbr.parentNode.removeChild(spchbr);
		document.getElementById("batMsg").innerHTML  = "";
	}
	else{
		document.getElementById("batMsg").innerHTML  = "";
	}
}

function recreate(){
	dch = document.createElement('div');
	dch.id = 'yolo';
	dch.setAttribute('class','input-group');

	spanch = document.createElement('span');
	spanch.setAttribute('class','input-group-addon');

	ich = document.createElement('i');
	ich.setAttribute('class','glyphicon glyphicon-home')

	spanch.appendChild(ich);

	inpp = document.createElement('input');
	inpp.type= 'text';
	inpp.name = 'nch';
	inpp.id = 'chambre';
	inpp.placeholder = "Numéro de chambre (facultatif)";
	inpp.setAttribute('class','form-control');


	dch.appendChild(spanch);
	dch.appendChild(inpp);
	return(dch);
}

function autreBat(batiment){
	if(batiment.value === "autre"){
		ddv = document.createElement('div');
		ddv.setAttribute('class','input-group');
		ddv.id = 'divaddr';

		spanaddr = document.createElement('span');
		spanaddr.setAttribute('class',"input-group-addon");

		iaddr= document.createElement('i');
		iaddr.setAttribute('class', "glyphicon glyphicon-home");

		spanaddr.appendChild(iaddr);


		addr = document.createElement('input');
		addr.setAttribute('class','form-control');
	    addr.id = 'addr';
	    addr.type = 'text';
	    addr.name = 'addr';
	    addr.placeholder = "Adresse"

	    spip = document.createElement('span');
	    spip.id = "spip";
	    spip.setAttribute("class","span-warning");

	    ddv.appendChild(spanaddr);
	    ddv.appendChild(addr);
	   

	    mf.insertBefore(ddv,document.getElementById("sbm"));7
	    ddv.parentNode.insertBefore(spip,ddv.nextSibling);

	    inp = document.getElementById('addr');
    	inp.addEventListener('blur',function(e){
        	verifadd(inp,e);
      	})

      	batiment.addEventListener('blur',function(e){
      		verinp = document.getElementById('addr');
      		if(batiment.value !== "autre"){
      			if(typeof(verinp)!= 'undefined' && verinp != null){
        			mf.removeChild(document.getElementById('divaddr'));
        			mf.removeChild(document.getElementById('spip'));
        			mf.insertBefore(recreate(),sbm);
        			spp = document.createElement('span');
					spp.id = "spanchbr";
					spp.setAttribute("class","span-warning");
					mf.insertBefore(spp,sbm);
        			
        			chambre_recreated = document.getElementById('chambre');
        			chambre_recreated.addEventListener('blur',function(e){
        				verifch(chambre_recreated,e);
        				autreBat(batiment);
        			})
        		}
        	}
      	})
	}
}

function verifch(chambre,e){
	if(isNaN(parseInt(chambre.value))){
		warning = "Il est conseillé de mettre un numéro de chambre";
		document.getElementById('spanchbr').innerHTML= warning;
	}
	else{
		document.getElementById('spanchbr').innerHTML = "";
	}
}

var cch = chambre;
var verinp = 0;
var dvch = 0;


mff.addEventListener('submit',function(e){
	cch = document.getElementById('chambre');
	verifLastName(nom,e);
	verifFirstName(prenom,e);
	verifpseudo(pseudo,e);
	verifpass(pass,passconf,e);
	verifmail(email,e);
	verifbat(batiment,e);
	if(typeof(cch)!= 'undefined' && cch != null){
		verifch(chambre,e)
	}
});

chambre.addEventListener('blur',function(e){
	verifch(chambre,e);
	autreBat(batiment);
})


batiment.addEventListener('blur',function(e){
	verifbat(batiment,e);
	autreBat(batiment);
})

email.addEventListener('blur',function(e){
	verifmail(email,e);
})

nom.addEventListener('blur', function(e){
	verifLastName(nom,e);
})

prenom.addEventListener('blur',function(e){
	verifFirstName(prenom,e);
})

pseudo.addEventListener('blur',function(e){
	verifpseudo(pseudo,e);
})

passconf.addEventListener('blur',function(e){
	verifpass(pass,passconf,e);
})

pass.addEventListener('blur',function(e){
	if(pass.value.length< 8){
		warning = "Le mot de pass doit contenir au moins 7 caractères";
		document.getElementById("passMsg").innerHTML = warning;
		e.preventDefault();
	}
	else{
		document.getElementById("passMsg").innerHTML  = "";
	}
})
/*
*/

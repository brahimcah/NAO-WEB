<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
      
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <link href="css/bootstrap.min.css" rel="stylesheet" media="screen">
    <style>
        html {
          height: 100vh;
        display: flex;        
        justify-content: center;
        text-align: center;
        }
        body {display: inline-block;}
        #snackbar {
  visibility: hidden;
  min-width: 250px;
  margin-left: -125px;
  background-color: rgb(6, 179, 15);
  color: rgb(0, 0, 0);
  text-align: center;
  border-radius: 2px;
  padding: 16px;
  position: fixed;
  z-index: 1;
  left: 50%;
  bottom: 30px;
  font-size: 17px;
}

#snackbar.show {
  visibility: visible;
  -webkit-animation: fadein 0.5s, fadeout 0.5s 2.5s;
  animation: fadein 0.5s, fadeout 0.5s 2.5s;
}

@-webkit-keyframes fadein {
  from {bottom: 0; opacity: 0;} 
  to {bottom: 30px; opacity: 1;}
}

@keyframes fadein {
  from {bottom: 0; opacity: 0;}
  to {bottom: 30px; opacity: 1;}
}

@-webkit-keyframes fadeout {
  from {bottom: 30px; opacity: 1;} 
  to {bottom: 0; opacity: 0;}
}

@keyframes fadeout {
  from {bottom: 30px; opacity: 1;}
  to {bottom: 0; opacity: 0;}
}
    </style>
</head>
<body>
  
    <h1 align="center">NAO </h1>
    <script src="https://code.jquery.com/jquery.js"></script>
    <br>
    <h3>    INFORMACI?? IMPORTANT PER L'USUARI</h3>
    <p>Aquesta aplicaci?? genera un arxiu amb la IP i el text per poder connectar i fer que el robot interactu??. Aquest arxiu es guarden en el servidor on s'allotgi el servidor web i Python.</p>
    <p>En cap moment l'aplicaci?? et pot demanar usuari, contrasenya, ni la vinculaci?? de cap compte.</p>
    <p>Tampoc realitza estad??stiques, no fa servir galetes pel seu funcionament.</p>
  
    <div>



<button align="center" onclick="window.location.href='./_ip'">He llegit la informaci??</button>
</div>
    <br><br>
    <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Licencia de Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">NAO-APP</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">JAUME SALA, IAN BRAHIM CHAHBOUNI</span> is licensed under a <BR><a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Reconocimiento-NoComercial-CompartirIgual 4.0 Internacional License</a>.  </ul>
    <ul>
    </div>
    <p>INS PLA DE L'ESTANY</p>


</html>

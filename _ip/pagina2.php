<html>

<head>
  <title>NAO</title>
</head>

<body>
  <?php
  $ar = fopen("../data/ip.txt", "r+") or
    die("Problemas en la creacion");
  fputs($ar, $_REQUEST['nombre']);
  fclose($ar);
  echo "Se ha afegit la IP correctament";
  ?>

  <meta http-equiv="refresh" content="1;url=..\Scripts" />

</body>

</html>
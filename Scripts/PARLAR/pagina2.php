<html>

<head>
  <title>NAO</title>
</head>

<body>
  <?php
  $ar = fopen("../../data/stext.txt", "r+") or
    die("Problemas en la creacion");
  fputs($ar, $_REQUEST['nombre']);
  fclose($ar);
  echo "Se ha añadido el IP correctamente";
  ?>
    <meta http-equiv="refresh" content="5;url=parlar.php" />

</body>

</html>
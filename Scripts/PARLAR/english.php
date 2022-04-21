<?php
    $command = escapeshellcmd('C:/Users/brahimcah/AppData/Local/Programs/Python/Python310/python.exe english.py');
    $output = shell_exec($command);
    echo $output;
?>
<meta http-equiv="refresh" content="1;url=./" />
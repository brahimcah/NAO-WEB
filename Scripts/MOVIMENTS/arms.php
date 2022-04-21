<?php
    $command = escapeshellcmd('C:/Users/brahimcah/AppData/Local/Programs/Python/Python310/python.exe arms.py');
    $output = shell_exec($command);
    echo $output;
    
?>
<meta http-equiv="refresh" content="5;url=./" />
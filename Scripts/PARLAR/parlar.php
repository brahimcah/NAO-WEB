<?php
    $command = escapeshellcmd('C:/Users/brahimcah/AppData/Local/Programs/Python/Python310/python.exe parlar.py');
    $output = shell_exec($command);
    echo $output;
?>
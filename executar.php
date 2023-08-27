<?php

$command = escapeshellcmd('python3 codigo.py -SEMA 5 0 0');
$output = shell_exec($command);
echo $output;

?>

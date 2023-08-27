<?php
echo 'ESTOU AQUI';
$command = escapeshellcmd('sudo python3 teste.py -SEMA 5 0 0');
echo 'ESTOU AQUI 1';
$output = shell_exec($command);
echo 'ESTOU AQUI 2!';
echo $output;

?>

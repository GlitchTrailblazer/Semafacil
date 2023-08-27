<?php

$command = './python3 codigo.py -SEMA 5 0 0';
exec($command, $out, $status);

echo $out;
echo $status;

?>

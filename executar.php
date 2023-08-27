<?php

$sema_verde = $_POST['sema_verde'] ?? '0';
$sema_amarelo = $_POST['sema_amarelo'] ?? '0';
$sema_vermelho = $_POST['sema_vermelho'] ?? '0';

$semb_verde = $_POST['semb_verde'] ?? '0';
$semb_amarelo = $_POST['semb_amarelo'] ?? '0';
$semb_vermelho = $_POST['semb_vermelho'] ?? '0';

$cmd = "python3 teste.py";

if ($sema_verde || $sema_amarelo || $sema_vermelho) {
    $cmd .= " -SEMA $sema_verde $sema_amarelo $sema_vermelho";
}
if ($semb_verde || $semb_amarelo || $semb_vermelho) {
    $cmd .= " -SEMB $semb_verde $semb_amarelo $semb_vermelho";
}

shell_exec($cmd);

// Redirecionar para o index após a execução
header("Location: index.html");
exit();
?>

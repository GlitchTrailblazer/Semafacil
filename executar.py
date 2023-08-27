#!/usr/bin/env python3
import cgi
import subprocess

# Lê os dados do formulário
form = cgi.FieldStorage()
sema_verde = form.getvalue('sema_verde', '0')
sema_amarelo = form.getvalue('sema_amarelo', '0')
sema_vermelho = form.getvalue('sema_vermelho', '0')

semb_verde = form.getvalue('semb_verde', '0')
semb_amarelo = form.getvalue('semb_amarelo', '0')
semb_vermelho = form.getvalue('semb_vermelho', '0')

# Chama o programa de semáforos com os parâmetros
cmd = ['python3', 'codigo.py']
if sema_verde or sema_amarelo or sema_vermelho:
    cmd.extend(['-SEMA', sema_verde, sema_amarelo, sema_vermelho])
if semb_verde or semb_amarelo or semb_vermelho:
    cmd.extend(['-SEMB', semb_verde, semb_amarelo, semb_vermelho])

subprocess.run(cmd)

# Redireciona para uma página de confirmação
print("Content-type: text/html\n")
print("<html><body>")
print("<h1>Execução concluída</h1>")
print("</body></html>")

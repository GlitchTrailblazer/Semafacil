import RPi.GPIO as GPIO
import time
import argparse
import signal
import sys

# Função para ligar um LED específico
def ligar_led(pino, duracao):
    GPIO.output(pino, True)
    time.sleep(duracao)
    GPIO.output(pino, False)

# Função para fazer uma luz piscar intermitentemente
def intermitente(pino, duracao_total, intervalo):
    inicio = time.time()
    while time.time() - inicio < duracao_total:
        GPIO.output(pino, True)
        time.sleep(intervalo)
        GPIO.output(pino, False)
        time.sleep(intervalo)

# Função para determinar se o valor contém "i" para intermitência
def is_intermitente(valor):
    return valor[-1] == "i"

# Configuração dos argumentos da linha de comando
parser = argparse.ArgumentParser(description="Controlar os semáforos.")
parser.add_argument("-SEMA", nargs=3, metavar=("tempo_verde", "tempo_amarelo", "tempo_vermelho"), help="Configuração do semáforo A (verde, amarelo, vermelho)")
parser.add_argument("-SEMB", nargs=3, metavar=("tempo_verde", "tempo_amarelo", "tempo_vermelho"), help="Configuração do semáforo B (verde, amarelo, vermelho)")
parser.add_argument("-intermitente", type=str, nargs=2, metavar=("pino", "duracao_total"), help="Fazer um LED piscar intermitentemente por um período de tempo (adicionar 'i' após o tempo)")

args = parser.parse_args()

# Mapeamento dos pinos dos semáforos A e B
pino_semaforos = {
    "A": {"verde": 14, "amarelo": 15, "vermelho": 18},
    "B": {"verde": 16, "amarelo": 20, "vermelho": 21}
}

# Verificar se algum argumento foi inserido
if not (args.SEMA or args.SEMB or args.intermitente):
    print("Erro: Nenhuma configuração de semáforo inserida. Use os argumentos -SEMA ou -SEMB para configurar os semáforos.")
    print("Exemplo: python3 codigo.py -SEMA 5 2 3 -SEMB 4 1 2")
    sys.exit(1)

# Configuração
GPIO.setmode(GPIO.BCM)
for semaforo in pino_semaforos.values():
    GPIO.setup(semaforo["verde"], GPIO.OUT)
    GPIO.setup(semaforo["amarelo"], GPIO.OUT)
    GPIO.setup(semaforo["vermelho"], GPIO.OUT)

# Desligar todas as luzes quando o usuário encerra a demonstração
def desligar_todas_luzes(sinal, quadro):
    for semaforo in pino_semaforos.values():
        GPIO.output(semaforo["verde"], False)
        GPIO.output(semaforo["amarelo"], False)
        GPIO.output(semaforo["vermelho"], False)
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, desligar_todas_luzes)

# Acender as luzes especificadas em ambos os semáforos
for semaforo, pinos in pino_semaforos.items():
    if semaforo == "A" and args.SEMA:
        verde, amarelo, vermelho = args.SEMA
    elif semaforo == "B" and args.SEMB:
        verde, amarelo, vermelho = args.SEMB
    else:
        continue
    
    if verde:
        if is_intermitente(verde):
            intermitente(pinos["verde"], int(verde[:-1]), 0.5)  # Piscar intermitentemente por 0.5 segundos
        else:
            ligar_led(pinos["verde"], int(verde))
    if amarelo:
        if is_intermitente(amarelo):
            intermitente(pinos["amarelo"], int(amarelo[:-1]), 0.5)  # Piscar intermitentemente por 0.5 segundos
        else:
            ligar_led(pinos["amarelo"], int(amarelo))
    if vermelho:
        if is_intermitente(vermelho):
            intermitente(pinos["vermelho"], int(vermelho[:-1]), 0.5)  # Piscar intermitentemente por 0.5 segundos
        else:
            ligar_led(pinos["vermelho"], int(vermelho))

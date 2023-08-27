import RPi.GPIO as GPIO
import time
import argparse
import signal
import sys

# Função para ligar um LED específico
def ligar_led(pino, duracao):
    GPIO.output(pino, GPIO.HIGH)
    time.sleep(duracao)
    GPIO.output(pino, GPIO.LOW)

# Configuração dos argumentos da linha de comando
parser = argparse.ArgumentParser(description="Controlar os semáforos.")
parser.add_argument("-SEMA", nargs=3, type=int, metavar=("tempo_verde", "tempo_amarelo", "tempo_vermelho"), help="Configuração do semáforo A (verde, amarelo, vermelho)")
parser.add_argument("-SEMB", nargs=3, type=int, metavar=("tempo_verde", "tempo_amarelo", "tempo_vermelho"), help="Configuração do semáforo B (verde, amarelo, vermelho)")

args = parser.parse_args()

# Mapeamento dos pinos dos semáforos A e B
pino_semaforos = {
    "A": {"verde": 14, "amarelo": 15, "vermelho": 18},
    "B": {"verde": 16, "amarelo": 20, "vermelho": 21}
}

# Verificar se algum argumento foi inserido
if not (args.SEMA or args.SEMB):
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
        ligar_led(pinos["verde"], verde)
    if amarelo:
        ligar_led(pinos["amarelo"], amarelo)
    if vermelho:
        ligar_led(pinos["vermelho"], vermelho)

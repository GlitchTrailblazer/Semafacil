import RPi.GPIO as GPIO
import time
import argparse
import signal
import sys

# Função para acender uma luz específica
def turn_on_light(pin, duration):
    GPIO.output(pin, True)
    time.sleep(duration)
    GPIO.output(pin, False)

# Configuração dos argumentos da linha de comando
parser = argparse.ArgumentParser(description="Control the traffic lights.")
parser.add_argument("-semaforo", choices=["A", "B"], required=True, help="Escolher semáforo (A ou B)")
parser.add_argument("-verde", type=int, help="Tempo para luz verde")
parser.add_argument("-amarelo", type=int, help="Tempo para luz amarela")
parser.add_argument("-vermelho", type=int, help="Tempo para luz vermelha")

args = parser.parse_args()

# Mapeamento dos pinos dos semáforos
semaforo_pins = {
    "A": {"verde": 14, "amarelo": 15, "vermelho": 18},
    "B": {"verde": 16, "amarelo": 20, "vermelho": 21}
}

# Configuração do semáforo selecionado
semaforo = semaforo_pins[args.semaforo]

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(semaforo["verde"], GPIO.OUT)
GPIO.setup(semaforo["amarelo"], GPIO.OUT)
GPIO.setup(semaforo["vermelho"], GPIO.OUT)

# Turn off all lights when user ends demo
def allLightsOff(signal, frame):
        GPIO.output(semaforo["verde"], False)
        GPIO.output(semaforo["amarelo"], False)
        GPIO.output(semaforo["vermelho"], False)
        GPIO.cleanup()
        sys.exit(0)

signal.signal(signal.SIGINT, allLightsOff)

# Acender as luzes especificadas
if args.verde:
    turn_on_light(semaforo["verde"], args.verde)
if args.amarelo:
    turn_on_light(semaforo["amarelo"], args.amarelo)
if args.vermelho:
    turn_on_light(semaforo["vermelho"], args.vermelho)

import RPi.GPIO as GPIO
import time
import argparse
import signal
import sys

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)  # Pino para a luz vermelha
GPIO.setup(15, GPIO.OUT)  # Pino para a luz âmbar
GPIO.setup(14, GPIO.OUT)  # Pino para a luz verde

# Função para acender uma luz específica
def turn_on_light(pin, duration):
    GPIO.output(pin, True)
    time.sleep(duration)
    GPIO.output(pin, False)

# Configuração dos argumentos da linha de comando
parser = argparse.ArgumentParser(description="Control the traffic light.")
parser.add_argument("-vermelha", action="store_true", help="Acender luz vermelha")
parser.add_argument("-amarela", action="store_true", help="Acender luz amarela")
parser.add_argument("-verde", action="store_true", help="Acender luz verde")
parser.add_argument("-tempo", type=int, default=3, help="Tempo que a luz ficará acesa")

args = parser.parse_args()

# Turn off all lights when user ends demo
def allLightsOff(signal, frame):
        GPIO.output(18, False)
        GPIO.output(15, False)
        GPIO.output(14, False)
        GPIO.cleanup()
        sys.exit(0)

signal.signal(signal.SIGINT, allLightsOff)

# Acender a luz especificada
if args.vermelha:
    turn_on_light(18, args.tempo)
elif args.amarela:
    turn_on_light(15, args.tempo)
elif args.verde:
    turn_on_light(14, args.tempo)

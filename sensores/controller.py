from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from RPi import GPIO
import sys
import time
from time import sleep
import Adafruit_DHT

sensoresRoute = Blueprint('sensoresRoute', __name__)

from main import app

@sensoresRoute.route('/activarSensorMovimiento', methods=['GET'])
def activarSensorMovimiento():
    #GPIO
    #activar = request.args.get('sensorMov')
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO_TRIGGER = 2
    GPIO_ECHO = 17
    PIN_LED = 5

    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_LED, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
    GPIO.output(GPIO_TRIGGER, False)
    
    contador = 0
    while contador < 10:
        GPIO.output(GPIO_TRIGGER, True)
        sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)
	start = time.time()
        while GPIO.input(GPIO_ECHO) == 0:
            start = time.time()
        while GPIO.input(GPIO_ECHO) == 1:
            stop = time.time()
        elapsed = stop-start
        distance = (elapsed * 34300)/2
        print (distance)
        if distance < 6:
            GPIO.output(PIN_LED, True)
        else:
            GPIO.output(PIN_LED, False)
        sleep(1)
        contador = contador + 1

    print ("Quit")
    GPIO.cleanup()
    res = {
        'estado': 'Funciona'
    }
    return jsonify(res)

@sensoresRoute.route('/tomarTemperatura', methods=['GET'])
def activarSensorTemperatura():
    #GPIO
    # Configuracion del tipo de sensor DHT
    sensor = Adafruit_DHT.DHT11
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    # Configuracion del puerto GPIO al cual esta conectado  (GPIO 23)
    pin = 23
    GPIO.setup(pin, GPIO.IN)

    # Ciclo principal infinito
    # Obtiene la humedad y la temperatura desde el sensor 
    humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
    if humedad is not None and temperatura is not None:
        # Imprime en la consola las variables temperatura y humedad con un decimal
        print('Temperatura={0:0.1f}*  Humedad={1:0.1f}%'.format(temperatura, humedad))
    else:
        print('Fallo en obtener la lectura. Intente de nuevo.')
    GPIO.cleanup()
    resultado = 'Temperatura={0:0.1f}*  Humedad={1:0.1f}%'.format(temperatura, humedad)
    res = {
        'estado': resultado
    }
    return jsonify(res)
from flask import request, jsonify,Blueprint, abort
from flask.views import MethodView
from RPi import GPIO
from time import sleep

servosRoute = Blueprint('servosRoute', __name__)

from main import app

@servosRoute.route('/abrirPersiana1', methods=['GET'])
def abrirPersiana1():
    #GPIO
    PIN = 12
    cant = 1
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)
	
    servo = GPIO.PWM(PIN, 50)
    servo.start(5)
    sleep(1)
    while cant < 2:
        servo.ChangeDutyCycle(5)
        sleep(0.5)
        cant = cant + 1

    servo.stop()
    GPIO.cleanup()
    res = {
        'estado': 'Abierta'
    }
    return jsonify(res)

@servosRoute.route('/cerrarPersiana1', methods=['GET'])
def cerrarPersiana1():
    #GPIO
    PIN = 12
    cant = 1
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)
	
    servo = GPIO.PWM(PIN, 50)
    servo.start(7)
    sleep(1)

    while cant < 3:
        servo.ChangeDutyCycle(10)
        sleep(0.5)
        cant = cant + 1

    servo.stop()
    GPIO.cleanup()
    res = {
        'estado': 'Cerrada'
    }
    return jsonify(res)

@servosRoute.route('/abrirPersiana2', methods=['GET'])
def abrirPersiana2():
   #GPIO
    PIN = 25

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)
	
    servo = GPIO.PWM(PIN, 50)
    servo.start(7)
    sleep(1)

    servo.ChangeDutyCycle(10)
    sleep(1)
    servo.stop()
    GPIO.cleanup()
    res = {
        'estado': 'Abierta'
    }
    return jsonify(res)

@servosRoute.route('/cerrarPersiana2', methods=['GET'])
def cerrarPersiana2():
    #GPIO
    PIN = 25

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)

    servo = GPIO.PWM(PIN, 50)
    servo.start(5)
    sleep(1)
	
    servo.stop()
    GPIO.cleanup()
    res = {
        'estado': 'Cerrada'
    }
    return jsonify(res)

@servosRoute.route('/abrirPuertaGaraje', methods=['GET'])
def abrirPuertaGaraje():
    #GPIO
    PIN = 21
    cant = 1
	
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)
		
    servo = GPIO.PWM(PIN, 50)
    servo.start(5)
    sleep(1)
    while cant < 2:
        servo.ChangeDutyCycle(5)
        sleep(0.5)
        cant = cant + 1
    servo.stop()
    GPIO.cleanup()
    res = {
        'estado': 'Abierta'
    }
    return jsonify(res)

@servosRoute.route('/cerrarPuertaGaraje', methods=['GET'])
def cerrarPuertaGaraje():
    #GPIO
    PIN = 21
    cant = 1
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)
		
    servo = GPIO.PWM(PIN, 50)
    servo.start(7)
    sleep(1)
    while cant < 4:
        servo.ChangeDutyCycle(10)
        sleep(0.5)
        cant = cant + 1
    
    servo.stop()
    GPIO.cleanup()
    res = {
        'estado': 'Cerrada'
    }
    return jsonify(res)

@servosRoute.route('/abrirPuertaPrincipal', methods=['GET'])
def abrirPuertaPrincipal():
   #GPIO
    PIN = 20

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)
	
    servo = GPIO.PWM(PIN, 50)
    servo.start(7)
    sleep(1)

    servo.ChangeDutyCycle(10)
    sleep(1)
    servo.stop()
    GPIO.cleanup()
    res = {
        'estado': 'Abierta'
    }
    return jsonify(res)

@servosRoute.route('/cerrarPuertaPrincipal', methods=['GET'])
def cerrarPuertaPrincipal():
    #GPIO
    PIN = 20

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)

    servo = GPIO.PWM(PIN, 50)
    servo.start(5)
    sleep(1)
	
    servo.stop()
    GPIO.cleanup()
    res = {
        'estado': 'Cerrada'
    }
    return jsonify(res)

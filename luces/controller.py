from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from RPi import GPIO
from time import sleep

lucesRoute = Blueprint('lucesRoute', __name__)

from main import app

@lucesRoute.route('/encenderLuzP1', methods=['GET'])
def encenderLuzP1():
    #GPIO
    PIN = 26

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, True)
    res = {
        'estado': 'Encendida'
    }
    return jsonify(res)


@lucesRoute.route('/apagarLuzP1', methods=['GET'])
def apagarLuzP1():
    #GPIO
    PIN = 26

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, False)
    res = {
        'estado': 'Apagada'
    }
    return jsonify(res)

@lucesRoute.route('/encenderLuzP2', methods=['GET'])
def encenderLuzP2():
    #GPIO
    PIN = 19

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, True)
    res = {
        'estado': 'Encendida'
    }
    return jsonify(res)

@lucesRoute.route('/apagarLuzP2', methods=['GET'])
def apagarLuzP2():
    #GPIO
    PIN = 19

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, False)
    res = {
        'estado': 'Apagada'
    }
    return jsonify(res)

@lucesRoute.route('/encenderLuzP3', methods=['GET'])
def encenderLuzP3():
    #GPIO
    PIN = 13

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, True)
    res = {
        'estado': 'Encendida'
    }
    return jsonify(res)

@lucesRoute.route('/apagarLuzP3', methods=['GET'])
def apagarLuzP3():
    #GPIO
    PIN = 13

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, False)
    res = {
        'estado': 'Apagada'
    }
    return jsonify(res)

@lucesRoute.route('/encenderLuzP4', methods=['GET'])
def encenderLuzP4():
    #GPIO
    PIN = 6

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, True)
    res = {
        'estado': 'Encendida'
    }
    return jsonify(res)

@lucesRoute.route('/apagarLuzP4', methods=['GET'])
def apagarLuzP4():
    #GPIO
    PIN = 6

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN, False)
    res = {
        'estado': 'Apagada'
    }
    return jsonify(res)

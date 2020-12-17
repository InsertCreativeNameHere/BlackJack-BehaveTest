from behave import *
from mano import Mano
from mazo import Mazo

@given('una {mano} para agregar una carta')
def step(context,mano):
    context.mano = Mano(mano.split(";"))
    context.mazo = Mazo()

@when('repartidor me da una carta')
def step(context):
    context.mano.agregarCarta(context.mazo.robar_carta())

@then('el tamaño de mi mano ahora es {valor}')
def step(context,valor):
    assert str(len(context.mano.cartas)) == str(valor)

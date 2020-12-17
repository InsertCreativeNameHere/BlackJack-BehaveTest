from behave import *
from mano import Mano
from mazo import Mazo

@given('un mazo para jugar 21 y dos jugadores con una mano cada uno')
def step(context):
    context.mazo = Mazo()
    context.mano1 = Mano([])
    context.mano2 = Mano([])

@when('Inicia la partida')
def step(context):
    context.mazo.barajar()

@then('cada jugador recibe 2 cartas')
def step(context):
    context.mano1.agregarCarta(context.mazo.robar_carta())
    context.mano2.agregarCarta(context.mazo.robar_carta())
    context.mano1.agregarCarta(context.mazo.robar_carta())
    context.mano2.agregarCarta(context.mazo.robar_carta())

@then('la longitud de la mano de cada jugador es 2 y el tamaña del mazo es 48')
def step(context):
    print(len(context.mano1.cartas))
    assert (len(context.mano1.cartas) == 2 and len(context.mano2.cartas) == 2 and len(context.mazo.cartas) == 48)
from behave import *
from mano import Mano

@given('una {mano} para comprobar el valor sus cartas')
def step(context, mano):
    context.mano = Mano(mano.split(";"))

@when('el jugador calcula el valor de la mano')
def step(context):
    context.valor = context.mano.evaluar()

@then('el {valor} es verdadero para terminar o falso para seguir')
def step(context, valor):
    
    if(21-context.valor < 0):
        context.res = 1
    elif(21 - context.valor <= 4 ):
        context.res = 1
    else:
        context.res = 0

    assert str(context.res) == str(valor)

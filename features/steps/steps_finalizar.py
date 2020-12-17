from behave import *
from mano import Mano

@given('Una {mano} para comparar con otra mano')
def step(context,mano):
    mano2 = "(5, picas);(J, treboles)"
    context.mano1 = Mano(mano.split(";"))
    context.mano2 = Mano(mano2.split(";"))

@when('el repartidor suma las manos')
def step(context):
    context.valor1 = context.mano1.evaluar()
    context.valor2 = context.mano2.evaluar() 
    
@then('el repartidor compara los resultados')
def step(context):
    if(context.valor1 == context.valor2):
        context.res = 0
    else:
        resta1 = 21 - context.valor1
        resta2 = 21 - context.valor2
        if((resta1 >= 0 and abs(resta1) < abs(resta2)) or (resta2 < 0 and resta1 > 0)):
            context.res = 1
        elif((resta2 >= 0 and abs(resta2) < abs(resta1)) or (resta1 < 0 and resta2 > 0)):
            context.res = 2
        else:
            context.res = 0
        

@then('Selecciona al {valor:d} ganador')
def step(context, valor):
    print(context.res)
    assert context.res == valor

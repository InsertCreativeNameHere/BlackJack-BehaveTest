Feature: Repartir al inicio
    
    Como repartidor quiero entregar 2 cartas a cada jugador para iniciar el juego.

Scenario: repartir
Given un mazo para jugar 21 y dos jugadores con una mano cada uno
When Inicia la partida
Then cada jugador recibe 2 cartas
And la longitud de la mano de cada jugador es 2 y el tamaña del mazo es 48


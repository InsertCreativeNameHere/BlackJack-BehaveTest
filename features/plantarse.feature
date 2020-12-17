Feature: Terminar turno

    Como jugador quiero plantarme para finalizar el turno.
    
Scenario Outline: plantarme o no
Given una <mano> para comprobar el valor sus cartas 
When el jugador calcula el valor de la mano
Then el <valor> es verdadero para terminar o falso para seguir

Examples:
    | mano | valor |
    | (5, picas);(5, treboles)  | 0  | 
    | (9, corazones);(A, treboles)  | 1  |

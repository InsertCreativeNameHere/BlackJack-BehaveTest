Feature: determinar ganador

    Como repartidor quiero saber el valor de las manos para determinar quién gana. 

Scenario Outline: jugador ganador
Given Una <mano> para comparar con otra mano
When el repartidor suma las manos
Then el repartidor compara los resultados
And Selecciona al <valor> ganador

Examples:
    | mano | valor |
    | (5, picas);(J, treboles) | 0  | 
    | (9, corazones);(2, treboles)| 2  |
    | (10, diamantes);(K, picas) |1  |
    | (8, picas);(K, treboles)  | 1  |
    | (2, diamantes);(J, treboles);(7, treboles)| 1  |
    | (5, picas);(J, treboles);(3, treboles);(K, treboles)| 2  |     
    | (2, picas);(Q, treboles);(K, diamantes) | 2  |
    | (3, picas) | 2  |
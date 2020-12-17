Feature: Solicitar una carta mas para la mano
    
    Como jugador quiero solicitar una carta adicional para seguir jugando.

Scenario Outline: Tamaño de la mano
Given una <mano> para agregar una carta
When repartidor me da una carta
Then el tamaño de mi mano ahora es <valor>

Examples:
    | mano | valor |
    | (5, picas);(J, treboles)  | 3  | 
    | (9, corazones);(A, treboles)  | 3  |
    | (3, diamantes);(Q, picas)  | 3  |
    | (A, picas) | 2  |
    | (A, diamantes);(J, treboles)  | 3  |
    | (5, picas);(J, treboles);(3, treboles)  | 4  |     
    | (A, picas);(A, treboles);(A, diamantes)  | 4  |
    | (A, picas);(A, treboles);(A, diamantes);(Q, picas)  | 5  |
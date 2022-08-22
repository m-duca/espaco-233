# The script of the game goes in this file.

default endings = 0

# Definindo os personagens

define e = Character("Eileen")
define s = Character("ESMAUGUE", color="#ed5a64")

# Início do Jogo

label start:

    scene bg room

    show eileen happy

    "Medo do esmaugyee"
    s "{b}RAAAAURRRRR{/b}" 

    call doors

    return

label doors:

    scene bg doors
    call screen doors_test


    return

label end:
    if endings == 1:
        scene gato
    if endings == 2:
        scene mike
    if endings == 3:
        scene sully
    return
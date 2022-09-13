# The script of the game goes in this file.

# Definindo os personagens
define e = Character("Eileen")
define s = Character("ESMAUGUE", color="#ed5a64")


# Início do Jogo
label start:

    scene bg room

    show eileen happy

    "Medo do esmaugyee"
    s "{b}RAAAAURRRRR{/b}"
    $ go_to_next(possibilities_right)

    return



label corredor:
    scene bg doors
    call screen buttons_navigation
    "Corredor legal bonito formoso"
    return

label banheiro:
    scene button1
    call screen buttons_navigation
    "banheiro pinico"
    return

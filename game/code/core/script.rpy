# The script of the game goes in this file.
# Primeira parte do código

# Antes do Menu Principal
label splashscreen:
    # Controla o tempo de pausa
    $show_time = 2
    $hide_time = 1
    $transition = Pixellate(1, 10)

    # Aparece Logo Smaug
    show logo_smaug at truecenter with transition
    pause show_time

    # Desaparece Logo Smaug
    hide logo_smaug with transition
    pause hide_time

    # Aparece Logo 404
    show logo_404 at truecenter with transition
    pause show_time

    # Desaparece Logo 404
    hide logo_404 with transition
    pause hide_time

    return

# Início do Jogo
label start:

    jump introduction

    scene bg room

    show eileen happy

    "Medo do esmaugyee"
    s "{b}RAAAAURRRRR{/b}"
    $ go_to_next(possibilities_right)

    return



label corredor:
    scene bg doors
    call screen buttons_navigation(True, True, False, False, Vector(1543, 493), Vector(427, 493))
    "Corredor legal bonito formoso"
    return

label banheiro:
    scene button1
    call  screen buttons_navigation(False, False, True, True, 0, 0, Vector(800, 240), Vector(800, 600))
    "banheiro pinico"
    return

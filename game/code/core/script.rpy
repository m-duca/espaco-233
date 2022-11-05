# Primeira parte do código

# Antes do Menu Principal
label splashscreen:
    # Troque o volume para o valor inicial
    call initial_volume

    # Controla o tempo de pausa
    $show_time = 2
    $hide_time = 1
    $transition = Pixellate(1, 10)

    # Mostre o fundo e a screen de efeito scanline
    scene bg splashscreen with fade
    show screen scanline

    # Aparece Logo Smaug
    play sound glitch
    show logo_smaug at truecenter with transition
    pause show_time

    # Desaparece Logo Smaug
    hide logo_smaug with transition

    # Aparece Logo 404
    play sound glitch
    show logo_404 at truecenter with transition
    pause show_time

    return

# Início do Jogo
label start:

    # Pule para a introdução
    jump introduction

    return


# Testes point and click
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

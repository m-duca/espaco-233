default show_quick_menu = True

# Antes do Menu Principal
label splashscreen:

    python:
        decompress("splashscreen")
        compress("intro", "bg intro_", 4)
        #compress("buttons", "button_", 8)
        compress("ship", "bg ship_", 7)
        #compress("space", "bg space_", 1)
        #compress("characters", "character_", 2)

    $ show_quick_menu = True

    image b_splashscreen = "images/splashscreen_0.png"
    image logo_smaug = "images/splashscreen_1.png"
    image logo_404 = "images/splashscreen_2.png"

    # Troque o volume para o valor inicial
    call initial_volume

    # Controla o tempo de pausa
    $show_time = 2
    $hide_time = 1
    $transition = Pixellate(1, 10)

    # Mostre o fundo e a screen de efeito scanline
    scene b_splashscreen with fade
    show screen scanline

    # Aparece Logo Smaug
    play sound "sfxs/glitch.ogg" volume 0.08
    show logo_smaug at truecenter with transition
    pause show_time

    # Desaparece Logo Smaug
    hide logo_smaug with transition

    # Aparece Logo 404
    play sound "sfxs/glitch.ogg" volume 0.08
    show logo_404 at truecenter with transition
    pause show_time

    hide screen scanline

    $ compress("splashscreen", "splashscreen_", 4)

    return

# Início do Jogo
label start:

    jump introduction

    return

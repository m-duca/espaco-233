default show_quick_menu = True

# Antes do Menu Principal
label splashscreen:

    call initial_compression

    pause 1

    $ show_quick_menu = True

    # Troque o volume para o valor inicial
    call initial_volume

    # Controla o tempo de pausa
    $show_time = 2
    $hide_time = 1
    $transition = Pixellate(1, 10)

    # Mostre o fundo e a screen de efeito scanline
    scene splashscreen_0 with fade
    show screen scanline

    # Aparece Logo Smaug
    play sound "sfxs/glitch.ogg" volume 0.08
    show splashscreen_1 at truecenter with transition
    pause show_time

    # Desaparece Logo Smaug
    hide splashscreen_1 with transition

    # Aparece Logo 404
    play sound "sfxs/glitch.ogg" volume 0.08
    show splashscreen_2 at truecenter with transition
    pause show_time

    hide screen scanline

    return

label initial_compression:

    python:
        #decompress("splashscreen")
        #compress("intro", "bg intro_", 4)
        #compress("buttons", "button_", 8)
        #compress("ship", "bg ship_", 7)
        #compress("space", "bg space_", 1)
        #compress("characters", "character_", 2)

    return

# Início do Jogo
label start:

    python:
        #compress("splashscreen", "splashscreen_", 4)
        #decompress("intro")

    jump introduction

    return

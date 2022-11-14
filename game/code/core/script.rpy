# Antes do Menu Principal
label splashscreen:
    #python:
        #compress("logos", "logo_", 2)
        #compress("buttons", "button_", 8)


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
    play sound "sfxs/glitch.ogg" volume 0.55
    show logo_0 at truecenter with transition
    pause show_time

    # Desaparece Logo Smaug
    hide logo_0 with transition

    # Aparece Logo 404
    play sound "sfxs/glitch.ogg" volume 0.55
    show logo_1 at truecenter with transition
    pause show_time

    return

# Início do Jogo
label start:
    jump introduction
    return

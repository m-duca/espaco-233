transform bounce1:
    xalign 5.75 yalign 0.45
    linear 0.5 yalign 0.0
    linear 1.0 yalign 0.45
    repeat

transform bounce2:
    xalign -5.75 yalign 0.8
    linear 0.5 yalign 0.5
    linear 1.0 yalign 0.8
    repeat

label puzzle2:

    call steps

    $ decompress("objects")

    image b_puzzle2 = im.Scale("images/bg ship_5.png", 1920, 1080)

    if puzzle2_completed == False:
        image box1 = "images/object_0.png"
        image box2 = "images/object_0.png"

        show box1 at bounce1
        show box2 at bounce2

    scene b_puzzle2 with fade

    if puzzle2_completed == False:
        jump intro_puzzle2
    else:
        call screen buttons_navigation (True, False, False, False)

return

label intro_puzzle2:

    scene b_puzzle2 with fade

    image box1 = "images/object_0.png"
    image box2 = "images/object_0.png"

    show box1 at bounce1
    show box2 at bounce2

    i "Parece que o sistema de gravidade dessa sala de armazéns está desativado, que tal a senhorita tentar consertá-lo?"

    i "A alavanca está localizada logo a sua frente, no fim da sala."

    i "Aconselho a ter cuidado com as caixas e itens espalhados por aí."

    menu:
        "Tentar chegar ao fim da sala?"

        "SIM":
            jump do_puzzle2
        "NÃO":
            jump central

    return


label do_puzzle2:

    image b_puzzle2 = im.Scale("images/bg ship_5.png", 1920, 1080)

    scene b_puzzle2 with fade

    image box1 = "images/object_0.png"
    image box2 = "images/object_0.png"

    show box1 at bounce1
    show box2 at bounce2

    menu:
        "Uma caixa está vindo em sua direção!"

        "Desviar para a esquerda":
            l "Um pouco fácil."

        "Desviar para a direita":
            play sound "sfxs/voice/resmungo.ogg" volume 1.0
            jump intro_puzzle2

    scene b_puzzle2 with fade

    show box1 at bounce1
    show box2 at bounce2

    menu:
        "Um armário grande está se aproximando!"

        "Ir para baixo":
            l "Ufa! Essa foi por pouco..."

        "Ir para cima":
            play sound "sfxs/voice/resmungo.ogg" volume 1.0
            jump intro_puzzle2


    scene b_puzzle2 with fade

    show box1 at bounce1
    show box2 at bounce2

    menu:
        "Uma gaveta cheia de pregos começa a chegar perto!"

        "Correr":
            play sound "sfxs/voice/resmungo.ogg" volume 1.0
            jump intro_puzzle2

        "Ir calmamente":
            $ puzzle2_completed = True
            l "Pregos?! Tá de brincadeira comigo..."

    "Loren chega ao final da sala, conseguindo então apertar o botão e ativar o sistema de gravidade novamente."

    $ compress("objects", "object_", 1)
    jump central

    return

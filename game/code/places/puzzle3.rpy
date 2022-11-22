label puzzle3:

    #$ puzzle3_completed = True

    $ soma = int()

    image b_puzzle3 = im.Scale("images/bg ship_6.png", 1920, 1080)

    call steps

    scene bgship_6 with fade

    if puzzle3_completed == False:
        jump intro_puzzle3
    else:
        call screen buttons_navigation (False, False, True, False)

return


label intro_puzzle3:

    image b_puzzle3 = im.Scale("images/bg ship_6.png", 1920, 1080)

    scene b_puzzle3 with fade

    #play sound "sfxs/eletronicos.ogg"

    i "Essa é uma das salas de comando da nave, logo adiante há um computador usado para o gerenciamento do sistema."

    i "Creio que através dele você conseguirá acionar novamente as turbinas."

    jump mid_puzzle3

    return

label mid_puzzle3:

    image b_puzzle3 = im.Scale("images/bg ship_6.png", 1920, 1080)

    scene b_puzzle3 with fade

    "Loren liga o computador e então começa a acessar o sistema."

    "Ao acessar o controle das turbinas, ela se depara com uma distribuição de energia, que deve se feita de forma equilibrada."

    jump do_puzzle3

    return

label do_puzzle3:

    image b_puzzle3 = im.Scale("images/bg ship_6.png", 1920, 1080)

    scene b_puzzle3 with fade

    #Se selecionar qualquer opção soma na variável e desaparece a opção
    menu:
        "Progresso das Turbinas: 0\%"

        "Distribua 151\% de energia":
            play sound "sfxs/tecla 1.ogg"
            l "Começando devagar..."

        "Distribua 93\% de energia":
            play sound "sfxs/som ambiente.ogg"

        #Esse aqui
        "Distribua 116\% de energia":

            play sound "sfxs/som ambiente.ogg"

        #Esse aqui
        "Distribua 279\% de energia":
            play sound "sfxs/som ambiente.ogg"

        #Esse aqui
        "Distribua 67\% de energia":
            play sound "sfxs/som ambiente.ogg"

        #Esse aqui
        "Distribua 38\% de energia":
            play sound "sfxs/som ambiente.ogg"

        "Deixar para fazer depois":
            jump central

    scene b_puzzle3 with fade
    menu:
        "Progresso das Turbinas: 25\%"

        "Distribua 151\% de energia":
            play sound "sfxs/tecla 1.ogg"
            l "Começando devagar..."

        "Distribua 93\% de energia":
            play sound "sfxs/som ambiente.ogg"


        "Distribua 116\% de energia":
            play sound "sfxs/som ambiente.ogg"


        "Distribua 279\% de energia":
            play sound "sfxs/som ambiente.ogg"


        "Distribua 67\% de energia":
            play sound "sfxs/som ambiente.ogg"


        "Distribua 38\% de energia":
            play sound "sfxs/som ambiente.ogg"

        "Deixar para fazer depois":
            jump central

    scene b_puzzle3 with fade
    menu:
        "Progresso das Turbinas: 50\%"

        "Distribua 151\% de energia":
            play sound "sfxs/tecla 1.ogg"
            l "Começando devagar..."

        "Distribua 93\% de energia":
            play sound "sfxs/som ambiente.ogg"


        "Distribua 116\% de energia":
            play sound "sfxs/som ambiente.ogg"


        "Distribua 279\% de energia":
            play sound "sfxs/som ambiente.ogg"


        "Distribua 67\% de energia":
            play sound "sfxs/som ambiente.ogg"


        "Distribua 38\% de energia":
            play sound "sfxs/som ambiente.ogg"

        "Deixar para fazer depois":
            jump central

    scene b_puzzle3 with fade
    menu:
        "Progresso das Turbinas: 75\%"

        #"Distribua 5\% de energia":
            #play sound "sfxs/tecla 2.ogg"
            #$ puzzle3_completed = True
            #pause 0.5
            #play sound "sfxs/motor ligando.ogg"
            #pause 2.0
            #"Progresso das Turbinas: 100\%, acionando-as..."
            #l "Ufa! mais um problema resolvido."

        "Distribua 151\% de energia":
            play sound "sfxs/som ambiente.ogg"

        "Distribua 93\% de energia":
            play sound "sfxs/som ambiente.ogg"

        "Distribua 116\% de energia":
            play sound "sfxs/som ambiente.ogg"

        "Distribua 279\% de energia":
            play sound "sfxs/som ambiente.ogg"

        "Distribua 67\% de energia":
            play sound "sfxs/som ambiente.ogg"

        "Distribua 38\% de energia":
            $ if soma == 500
            play sound "sfxs/tecla 2.ogg"
            $ puzzle3_completed = True
            pause 0.5
            play sound "sfxs/motor ligando.ogg"
            pause 2.0
            "Progresso das Turbinas: 100\%, acionando-as..."
            l "Ufa! mais um problema resolvido."


        "Deixar para fazer depois":
            jump central


    jump central

    return

label puzzle3:

    #$ puzzle3_completed = True
    call steps

    image b_puzzle3 = im.Scale("images/bg ship_6.png", 1920, 1080)

    #scene black with fade
    scene b_puzzle3 with fade

    if puzzle3_completed == False:
        jump intro_puzzle3
    else:
        call screen buttons_navigation (False, False, True, False)

return


label intro_puzzle3:

    image b_puzzle3 = im.Scale("images/bg ship_6.png", 1920, 1080)

    #scene black with fade
    scene b_puzzle3 with fade

    #play sound "sfxs/eletronicos.ogg"

    i "Essa é uma das salas de comando da nave, logo adiante há um computador usado para o gerenciamento do sistema."

    i "Creio que através dele você conseguirá acionar novamente as turbinas."

    jump mid_puzzle3

    return

label mid_puzzle3:

    image b_puzzle3 = im.Scale("images/bg ship_6.png", 1920, 1080)

    #scene black with fade
    scene b_puzzle3 with fade

    "Loren liga o computador e então começa a acessar o sistema."

    "Ao acessar o controle das turbinas, ela se depara com uma distribuição de energia, que deve ser feita de forma equilibrada."

    i "Segundo o banco de dados da nave, o sistema se comporta bem com o valor 500."

    i "Tente alcançar este valor."


    jump do_puzzle3

    return

define option151 = False
define option93 = False
define option116 = False
define option279 = False
define option67 = False
define option38 = False
define soma = 0

label do_puzzle3:

    image b_puzzle3 = im.Scale("images/bg ship_6.png", 1920, 1080)

    #scene black with fade
    scene b_puzzle3 with fade

    #Se selecionar qualquer opção soma na variável e desaparece a opção
    menu:
        "Energia depositada: 0"

        "Distribua 151 de energia" if option151 == False:
            play sound "sfxs/tecla 1.ogg" volume 1.0
            $ option151 = True
            $ soma = soma + 151
            l "Começando devagar..."

        "Distribua 93 de energia" if option93 == False:
            play sound "sfxs/tecla 2.ogg" volume 1.0
            $ option93 = True
            $ soma = soma + 93
            l "Começando devagar..."

        #Esse aqui
        "Distribua 116 de energia" if option116 == False:
            play sound "sfxs/tecla 1.ogg" volume 1.0
            $ option116 = True
            $ soma = soma + 116
            l "Começando devagar..."

        #Esse aqui
        "Distribua 279 de energia" if option279 == False:
            play sound "sfxs/tecla 2.ogg" volume 1.0
            $ option279 = True
            $ soma = soma + 279
            l "Começando devagar..."

        #Esse aqui
        "Distribua 67 de energia" if option67 == False:
            play sound "sfxs/tecla 1.ogg" volume 1.0
            $ option67 = True
            $ soma = soma + 67
            l "Começando devagar..."

        #Esse aqui
        "Distribua 38 de energia" if option38 == False:
            play sound "sfxs/tecla 2.ogg" volume 1.0
            $ option38 = True
            $ soma = soma + 38
            l "Começando devagar..."

        "Deixar para fazer depois":
            python:
                option151 = False
                option93 = False
                option116 = False
                option279 = False
                option67 = False
                option38 = False
                soma = 0
            jump central

    scene b_puzzle3 with fade
    menu:
        "Energia depositada: [soma]"

        "Distribua 151 de energia" if option151 == False:
            play sound "sfxs/tecla 1.ogg" volume 1.0
            $ option151 = True
            $ soma = soma + 151

        "Distribua 93 de energia" if option93 == False:
            play sound "sfxs/tecla 2.ogg" volume 1.0
            $ option93 = True
            $ soma = soma + 93

        #Esse aqui
        "Distribua 116 de energia" if option116 == False:
            play sound "sfxs/tecla 1.ogg" volume 1.0
            $ option116 = True
            $ soma = soma + 116


        #Esse aqui
        "Distribua 279 de energia" if option279 == False:
            play sound "sfxs/tecla 2.ogg" volume 1.0
            $ option279 = True
            $ soma = soma + 279

        #Esse aqui
        "Distribua 67 de energia" if option67 == False:
            play sound "sfxs/tecla 1.ogg" volume 1.0
            $ option67 = True
            $ soma = soma + 67

        #Esse aqui
        "Distribua 38 de energia" if option38 == False:
            play sound "sfxs/tecla 2.ogg" volume 1.0
            $ option38 = True
            $ soma = soma + 38

        "Deixar para fazer depois":
            python:
                option151 = False
                option93 = False
                option116 = False
                option279 = False
                option67 = False
                option38 = False
                soma = 0
            jump central

    scene b_puzzle3 with fade
    menu:
        "Energia depositada: [soma]"

        "Distribua 151 de energia" if option151 == False:
            play sound "sfxs/tecla 1.ogg" volume 1.0
            $ option151 = True
            $ soma = soma + 151
            l "Quase lá!"

        "Distribua 93 de energia" if option93 == False:
            play sound "sfxs/tecla 2.ogg" volume 1.0
            $ option93 = True
            $ soma = soma + 93
            l "Quase lá!"

        #Esse aqui
        "Distribua 116 de energia" if option116 == False:
            play sound "sfxs/tecla 1.ogg" volume 1.0
            $ option116 = True
            $ soma = soma + 116
            l "Quase lá!"

        #Esse aqui
        "Distribua 279 de energia" if option279 == False:
            play sound "sfxs/tecla 2.ogg" volume 1.0
            $ option279 = True
            $ soma = soma + 279
            l "Quase lá!"

        #Esse aqui
        "Distribua 67 de energia" if option67 == False:
            play sound "sfxs/tecla 1.ogg" volume 1.0
            $ option67 = True
            $ soma = soma + 67
            l "Quase lá!"

        #Esse aqui
        "Distribua 38 de energia" if option38 == False:
            play sound "sfxs/tecla 2.ogg" volume 1.0
            $ option38 = True
            $ soma = soma + 38
            l "Quase lá!"

        "Deixar para fazer depois":
            python:
                option151 = False
                option93 = False
                option116 = False
                option279 = False
                option67 = False
                option38 = False
                soma = 0
            jump central

    scene b_puzzle3 with fade
    menu:
        "Energia depositada: [soma]"

        "Distribua 151 de energia" if option151 == False:
            play sound "sfxs/tecla 1.ogg" volume 1.0
            $ option151 = True
            $ soma = soma + 151

        "Distribua 93 de energia" if option93 == False:
            play sound "sfxs/tecla 2.ogg" volume 1.0
            $ option93 = True
            $ soma = soma + 93

        #Esse aqui
        "Distribua 116 de energia" if option116 == False:
            play sound "sfxs/tecla 1.ogg" volume 1.0
            $ option116 = True
            $ soma = soma + 116


        #Esse aqui
        "Distribua 279 de energia" if option279 == False:
            play sound "sfxs/tecla 2.ogg" volume 1.0
            $ option279 = True
            $ soma = soma + 279

        #Esse aqui
        "Distribua 67 de energia" if option67 == False:
            play sound "sfxs/tecla 2.ogg" volume 1.0
            $ option67 = True
            $ soma = soma + 67

        #Esse aqui
        "Distribua 38 de energia" if option38 == False:
            play sound "sfxs/tecla 1.ogg" volume 1.0
            $ option38 = True
            $ soma = soma + 38

        "Deixar para fazer depois":
            python:
                option151 = False
                option93 = False
                option116 = False
                option279 = False
                option67 = False
                option38 = False
                soma = 0
            jump central

    #Verifica se a soma final deu 500
    if soma != 500:
        python:
            option151 = False
            option93 = False
            option116 = False
            option279 = False
            option67 = False
            option38 = False
            soma = 0
        play sound "sfxs/som ambiente.ogg" volume 0.8
        jump mid_puzzle3
    else:
        play sound "sfxs/tecla 2.ogg" volume 1.0
        $ puzzle3_completed = True
        pause 0.5
        play sound "sfxs/motor ligando.ogg" volume 1.0
        pause 2.0
        "Progresso das Turbinas: 100\%, acionando-as..."
        l "Ufa! mais um problema resolvido."
        jump central

    return

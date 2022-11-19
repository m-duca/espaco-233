label puzzle3:

    #$ puzzle3_completed = True

    call steps

    scene black with fade

    if puzzle3_completed == False:
        jump intro_puzzle3
    else:
        call screen buttons_navigation (False, False, True, False)

return


label intro_puzzle3:
    scene black with fade
    
    i "Essa é uma das salas de comando da nave, logo adiante há um computador usado para o gerenciamento do sistema."

    i "Creio que através dele você conseguirá acionar novamente as turbinas."

    "Loren liga o computador e então começa a acessar o sistema."

    "Ao acessar o controle das turbinas, ela se depara com uma distribuição de energia, que deve se feita de forma equilibrada."

    jump do_puzzle3

    return


label do_puzzle3:
    scene black with fade
    menu:
        "Progresso das Turbinas: 0\%"

        "Distribua 5\% de energia":
            l "Começando devagar..."

        "Distribua 10\% de energia":
            jump intro_puzzle3

        "Distribua 20\% de energia":
            jump intro_puzzle3

        "Distribua 40\% de energia":
            jump intro_puzzle3

        "Deixar para fazer depois":
            jump central

    scene black with fade
    menu:
        "Progresso das Turbinas: 25\%"

        "Distribua 5\% de energia":
            jump intro_puzzle3

        "Distribua 10\% de energia":
            jump intro_puzzle3

        "Distribua 20\% de energia":
            l "Vamos estressar um pouquinho o sistema."

        "Distribua 40\% de energia":
            jump intro_puzzle3

        "Deixar para fazer depois":
            jump central

    scene black with fade
    menu:
        "Progresso das Turbinas: 50\%"

        "Distribua 5\% de energia":
            jump intro_puzzle3

        "Distribua 10\% de energia":
            l "Acho que é o suficiente."

        "Distribua 20\% de energia":
            jump intro_puzzle3

        "Distribua 40\% de energia":
            jump intro_puzzle3

        "Deixar para fazer depois":
            jump central

    scene black with fade
    menu:
        "Progresso das Turbinas: 75\%"

        "Distribua 5\% de energia":
            $ puzzle3_completed = True
            "Progresso das Turbinas: 100\%, acionando-as..."
            l "Ufa! mais um problema resolvido."

        "Distribua 10\% de energia":
            jump intro_puzzle3

        "Distribua 20\% de energia":
            jump intro_puzzle3

        "Distribua 40\% de energia":
            jump intro_puzzle3

        "Deixar para fazer depois":
            jump central


    jump central

    return

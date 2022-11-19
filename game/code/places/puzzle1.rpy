label puzzle1:

    call steps

    scene black with fade

    if puzzle1_completed == False:
        jump intro_puzzle1
    else:
        call screen buttons_navigation (False, False, False, True)

return

label intro_puzzle1:
    scene black with fade

    "Ao entrar na sala, Loren se depara com uma espécie de caixa de metal contendo fios cortados."

    "Há três fios: um amarelo, um rosa e um azul."

    jump do_puzzle1

    return

label do_puzzle1:

    "Ao entrar na sala, Loren se depara com uma espécie de caixa de metal contendo fios cortados."

    "Há três fios: um amarelo, um rosa e um azul."

    scene black with fade

    menu:
        "Escolha um dos fios soltos para conectar:"

        "Amarelo":
            jump intro_puzzle1

        "Rosa":
            l "Um já foi!"

        "Azul":
            jump intro_puzzle1

        "Deixar para fazer depois":
            jump central


    scene black with fade

    menu:
        "Escolha o próximo fio solto para conectar:"

        "Amarelo":
            l "Agora só resta o fio azul."

        "Azul":
            jump intro_puzzle1

        "Deixar para fazer depois":
            jump central

    scene black with fade
    menu:
        "Escolha o último fio solto para conectar:"

        "Azul":
            l "Ótimo! Deu tudo certo."
            $ puzzle1_completed = True


    jump central

    return

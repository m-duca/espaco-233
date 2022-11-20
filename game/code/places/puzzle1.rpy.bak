label puzzle1:

    call steps

    scene bgship_4 with fade

    if puzzle1_completed == False:
        jump intro_puzzle1
    else:
        call screen buttons_navigation (False, False, False, True)

return

label intro_puzzle1:
    scene bgship_4 with fade

    "Ao entrar na sala, Loren se depara com uma espécie de caixa de metal contendo fios cortados."

    "Há três fios: um amarelo, um rosa e um azul."

    jump do_puzzle1

    return

label do_puzzle1:

    scene bgship_4 with fade

    menu:
        "Escolha um dos fios soltos para conectar:"

        "Amarelo":
            play sound "sfxs/som ambiente.ogg"
            jump intro_puzzle1

        "Rosa":
            play sound "sfxs/click encaixe.ogg"
            l "Um já foi!"

        "Azul":
            play sound "sfxs/som ambiente.ogg"
            jump intro_puzzle1

        "Deixar para fazer depois":
            jump central


    scene bgship_4 with fade

    menu:
        "Escolha o próximo fio solto para conectar:"

        "Amarelo":
            play sound "sfxs/click encaixe.ogg"
            l "Agora só resta o fio azul."

        "Azul":
            play sound "sfxs/som ambiente.ogg"
            jump intro_puzzle1

        "Deixar para fazer depois":
            jump central

    scene bgship_4 with fade
    menu:
        "Escolha o último fio solto para conectar:"

        "Azul":
            play sound "sfxs/click encaixe.ogg"
            l "Ótimo! Deu tudo certo."
            $ puzzle1_completed = True


    jump central

    return

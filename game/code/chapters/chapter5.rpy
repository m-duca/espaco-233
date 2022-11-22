label chapter5:
    #compress("characters", "character_", 2)

    image b_space = im.Scale("images/bg space_0.png", 1920, 1080)
    scene b_space with fade

    "O oxigênio do traje começa a sair e não a mais nada que Loren possa fazer."

    play sound "sfxs/soldando.ogg"
    #tava escrito "e ele para de vazar." no final
    "Ela já tinha aceitado que seu fim estava próximo, mas como uma última esperança, corta um pedaço de seu traje e faz uma isolação com sucesso no tanque parando o vazamento."

    stop sound

    i "Senhorita rápido, volte imediatamente para a cabine não a tempo, ou a senhorita não irá sobreviver!"

    l "Não tem mais o que fazer Aiden, eu tenho dois rompimentos no meu traje, o oxigênio vai acabar mais rápido do que eu chegar até a porta."

    i "Mas isso não é possível, por favor ten..."

    l "Eu já aceitei que vou morrer aqui neste lugar depois de ter salvado todos."

    l "Foi um bom fim."

    l "{b}*Cof* *Cof*{/b} Obrigada Aiden você me ajudou muito a não me fazer sentir sozinha nesse lugar."

    i "Eu que agradeço a você Senhorita Loren, algum último pedido?"

    #Escolha final
    menu:

        "Conte o que aconteceu para a tripulação...":

            scene b_space with fade

            "Com isso Loren diz suas últimas palavras, para que não importa o que aconteça, todos se lembrem de quem ela foi."

            l "De tudo, desculpe mãe, e de nada a todos vocês da nave."

            l "{b}*Cof* *Cof*{/b} Há, verdade, e pra não esquecer, se fodam Saul e Tina."

            l "E também, até mais e obrigados pelos peixes."

        "Não falar nada...":

            "Loren decide partir em silencio à deriva no espaço."

            scene b_space with fade

    pause 3.0
    call credits

    scene b_space with fade

    return

label credits:
    window hide
    $ show_quick_menu = False
    $ credits_speed = 20
    #show bg splashscreen
    with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3.0)
    hide theend with dissolve
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(5.0)
    hide thanks with dissolve
    return


init python:
    credits = ('Caike Grion dos Santos', 'Game Design'), ('João Pedro Queiroz de Melo', 'Arte'), ('Lucas Neves Timar', 'Programação'), ('Lucas Proetti Quadros', 'Som'), ('Matheus Santos Duca', 'Programação')
    credits_s = "{size=80}EQUIPE 404\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]

init:
    image cred = Text(credits_s, font="space age.ttf", text_align=0.5)
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}FIM", text_align=0.5)
    image thanks = Text("{size=80}Obrigado por Jogar!", text_align=0.5)

transform aiden_bounce1:
    xalign 0.5 yalign 0.45
    linear 0.5 yalign 0.0
    linear 1.0 yalign 0.45
    repeat

label chapter2:

    call steps
    call fade_music

    $ decompress("loren")
    $ decompress("aiden")


    image b_instruction = im.Scale("images/bg ship_2.png", 1920, 1080)
    image b_central = im.Scale("images/bg ship_3.png", 1920, 1080)

    image aiden_idle = im.Scale("images/aiden_0.png", 1000, 1000)
    image aiden_worried = im.Scale("images/aiden_1.png", 1000, 1000)

    image loren_worried = im.Scale("images/loren_3.png", 800, 800)


    play sound "sfxs/porta nave.ogg" volume 1.0
    pause 3.0

    scene b_instruction with fade

    play music "musics/ambiente nave.ogg" fadein 1.0

    "Chegando na sala, está completamente sozinha, ela se sentia feliz pensando novamente estar adiantada e comemora levemente por sua conquista."

    play sound "sfxs/voice/risada.ogg" volume 0.95
    pause 1.0

    "Ao se sentar a apresentação começa automaticamente, ela estranha pois achava que mais pessoas deveriam chegar antes de tudo começar."

    "Ela levanta a mão e faz uma pergunta à inteligência artificial."

    show loren_worried at center with fade
    l "Com licença, não era pra ter mais pessoas aqui antes de começarem as explicações?"

    i2 "Desculpe senhorita Loren, mas todos que deveriam estar aqui já chegaram."

    play sound "sfxs/voice/pensativa.ogg" volume 1.0
    "Com receio, ela estranha totalmente a situação e sai da apresentação procurando por alguém."

    $ compress("loren", "loren_", 4)
    scene b_central with pushright

    "Ela corre desesperadamente e acha um ponto de informações e pergunta aonde estão todos, e tem uma resposta muito desagradável."

    show aiden_idle at aiden_bounce1 with fade
    i "Não há ninguém acordado."

    l "Como assim? E como eu posso estar acordada."

    i "Isso não seria possível pois faltam 712500000000000km para o destino final, ou seja, 80 anos."

    #scene b_central with vpunch

    play sound "sfxs/voice/surpresa.ogg" volume 1.0
    l "COMO ASSIM CARALHO, EU TÔ PRESA NO ESPAÇO POR UMA MERDA DE MÁ SORTE?"

    i "Não má sorte, ou talvez azar, mas pelo simples fato de… pelo fato de… desculpe, mas não sei o motivo de você estar acordada."

    l "Isso não importa mais, apenas me coloque pra dormir de novo."

    i "Claro, seria um prazer."

    play sound "sfxs/tecla 1.ogg" volume 1.0
    pause 1.0
    play sound "sfxs/tecla 2.ogg" volume 1.0
    pause 1.0
    play sound "sfxs/tecla 1.ogg" volume 1.0
    pause 1.0
    play sound "sfxs/tecla 2.ogg" volume 1.0
    pause 1.0
    play sound "sfxs/som ambiente.ogg" volume 0.9
    pause 1.0

    hide aiden_idle
    show aiden_worried at aiden_bounce1
    i "..."

    i "Opa, tenho um pequeno problema."

    l "Aaaa o que foi agora?"

    i "Eu não posso fazer isso."

    play sound "sfxs/voice/duvida.ogg" volume 1.0

    l "POR QUE NÃO?"

    i "Eu não tenho acesso as cabines de hibernação, e nenhuma delas poderia ativar ou desativar pois existem alguns problemas na nave."

    l "PROBLEMAS? Então eu faço o que agora, sento no chão e espero morrer com o tempo nessa nave?"


    hide aiden_worried
    show aiden_idle at aiden_bounce1

    i "Seria uma opção."

    play sound "sfxs/voice/resmungo.ogg" volume 1.0

    l "VAI CAGAR!"

    i "Ou a senhorita poderia arrumar os problemas na nave."

    l "De que jeito?"

    i "Vejo que a senhorita é formada em mecânica e também em engenharia avançada."

    i "Então dessa forma poderia com meu auxílio consertar todos os defeitos da nave, fazendo assim com que eu possa ativar sua cabine de hibernação e tudo ficar resolvido."

    l "Certo e como é que eu faço isso?"

    i "Apenas siga minhas instruções."

    scene b_central with fade

    hide aiden_worried
    show aiden_idle at aiden_bounce1
    i "Existem 3 erros ocorrendo atualmente na nave, e você pode consertá-los na ordem que quiser:"

    i "{b}1º{/b} Pelo visto o sistema de análises da nave está comprometido, é preciso localizar o problema e arrumar o que danificou o sistema."

    i "{b}2º{/b} Tem uma parte da nave onde o sistema de gravidade não está funcionando, fazendo com que objetos estejam flutuando por aí, podendo causar mais danos à nave."

    i "{b}3º{/b} Um dos propulsores da nave está falhando e desse jeito a nave não está em sua velocidade máxima."

    #Pelo visto o sistema de análise da nave está comprometido, e a porta que abre aquela ala não parece funcionar,
    #então você teria que descobrir um jeito de abrir a porta e depois arrumar o que danificou o sistema.

    i "Dessa forma eu recomendo que faça uma das duas primeiras opções que eu lhe dei, pois não queremos mais problemas."

    i "E se a nave não está a 100\% de velocidade, poderia não chegar a tempo em nosso destino por conta do combustível."

    l "Okay, okay, vamos lá."

    #scene b_central with fade

    $ compress("aiden", "aiden_", 4)
    #gameplay começa aqui
    jump central

    return

label chapter2:
    # CENAS: SALA DE INSTRUÇÕES (bg chapter2_0), AMBIENTE DA NAVE (bg chapter2_1)

    call fade_music

    play sound "sfxs/porta nave.ogg"
    pause 3.0

    scene black with fade
    #scene bg chapter2_0 with fade

    play music "musics/ambiente nave.ogg" fadein 1.0

    "Chegando na sala, está completamente sozinha, ela se sentia feliz pensando novamente estar adiantada e comemora levemente por sua conquista."

    play sound "sfxs/voice/risada.ogg"
    pause 1.0

    "Ao se sentar a apresentação começa automaticamente, ela estranha pois achava que mais pessoas deveriam chegar antes de tudo começar."

    "Ela levanta a mão e faz uma pergunta à inteligência artificial."

    l "Com licença, não era pra ter mais pessoas aqui antes de começarem as explicações?"

    i "Desculpe senhorita Loren, mas todos que deveriam estar aqui já chegaram."

    play sound "sfxs/voice/pensativa.ogg"
    "Com receio, ela estranha totalmente a situação e sai da apresentação procurando por alguém."

    scene black with hpunch
    #scene bg chapter2_1 with hpunch

    "Ela corre desesperadamente e acha um ponto de informações e pergunta aonde estão todos, e tem uma resposta muito desagradável."

    i "Não há ninguém acordado."

    l "Como assim? E como eu posso estar acordada."

    i "Isso não seria possível pois faltam 712500000000000km para o destino final, ou seja, 75 anos."

    scene black with vpunch
    #scene bg chapter2_1 with vpunch
    play sound "sfxs/voice/surpresa.ogg"
    l "COMO ASSIM CARALHO, EU TÔ PRESA NO ESPAÇO POR UMA MERDA DE MÁ SORTE?"

    i "Não má sorte, ou talvez azar, mas pelo simples fato de… pelo fato de… desculpe, mas não sei o motivo de você estar acordada."

    l "Isso não importa mais, apenas me coloque pra dormir de novo."

    i "Claro, seria um prazer."

    play sound "sfxs/tecla 1.ogg"
    pause 1.0
    play sound "sfxs/tecla 2.ogg"
    pause 1.0
    play sound "sfxs/tecla 1.ogg"
    pause 1.0
    play sound "sfxs/tecla 2.ogg"
    pause 1.0
    play sound "sfxs/som ambiente.ogg"
    pause 1.0

    i "..."

    i "Opa, tenho um pequeno problema."

    l "Aaaa o que foi agora?"

    i "Eu não posso fazer isso."

    l "PORQUE NÃO?"

    i "Eu não tenho acesso as cabines de hibernação, e nenhuma delas poderia ativar ou desativar pois existem alguns problemas na nave?"

    l "PROBLEMAS? Então eu faço o que agora, sento no chão e espero morrer com o tempo nessa nave?"

    i "Seria uma opção."

    l "VAI CAGAR!"

    i "Ou a senhorita poderia arrumar os problemas na nave."

    l "De que jeito?"

    i "Vejo que a senhorita é formada em mecânica e também em engenharia avançada."

    i "Então dessa forma poderia com meu auxílio consertar todos os defeitos da nave, fazendo assim com que eu possa ativar sua cabine de hibernação e tudo ficar resolvido."

    l "Certo e como é que eu faço isso?"

    i "Apenas siga minhas instruções."

    scene black with fade
    #scene bg chapter2_1 with fade

    i "Existem 3 erros ocorrendo atualmente na nave, e você pode consertá-los na ordem que quiser:"

    i "1º Um dos propulsores da nave está falhando e desse jeito a nave não está em velocidade máxima."

    i "2º Tem uma parte da nave onde o sistema de gravidade não está funcionando, fazendo com que objetos estejam flutuando por aí, podendo causar mais danos à nave."

    i "3º Pelo visto o sistema de análise da nave está comprometido, e a porta que abre aquela ala não parece funcionar, então você teria que descobrir um jeito de abrir a porta e depois arrumar o que danificou o sistema."

    i "Dessa forma eu recomendo que faça uma das duas primeiras opções que eu lhe dei, pois não queremos mais problemas."

    i "E se a nave não está a 100\% de velocidade, poderia não chegar a tempo em nosso destino por conta do combustível."

    l "Okay, okay, vamos lá."

    l "Qual eu devo escolher?"

    scene black with fade
    #scene bg chapter2_1 with fade

    #gameplay começa aqui

    return

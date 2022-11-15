label finalChapter:
    # CENAS: AMBIENTE DA NAVE (bg finalchapter_0), SAÍDAS DA NAVE (bg finachapter_1), CONSERTANDO O TANQUE (bg final_chapter2),
    # DESPEDIDA (bg finalchapter_3)

    call fade_music

    scene black with fade

    "Após todo o sufoco e determinação de Loren ela consegue consertar todos os defeitos encontrados na nave e sua esperança é finalmente restaurada, ela corre alegremente pelos corredores, pulando e saltitando pra lá e pra cá."

    l "Finalmente, meu deus, como foi difícil, mas até que enfim, vou poder voltar a dormir e VIVER, AEEEEE CARA..."

    i "Senhorita Loren!!!"

    l "Oi *nome da IA* fala meu chapa, vai me botar pra mimir finalmente, já está batendo a saudades, eu sei eu sei, eu vou sentir saudades também meu querido."

    i "Não é isso, mas eu receio que não acabou."

    l "NÃO ACABOU? Mas você disse que só tinham 3 problemas na nave, e agora não acabou?"

    i "Me desculpe, até aquele momento eu achava que só existiam aqueles defeitos, mas como o sistema estava danificado, eu não consegui identificar todos eles."

    l "DROGA!"

    l "Qual é o problema? Se for urgente me diz logo."

    i "Pelo jeito um dos tanques reservas está com um vazamento, e como é pequeno por isso não foi perceptível para mim sem a ajuda do sistema."

    i "Mas por conta de todo o tempo que estamos arrumando as outras partes da nave, o combustível já está quase acabando nesse tanque, e com isso se ele se esgotar eu não conseguirei te pôr novamente em sua cabine."

    l "QUAL É UNIVERSO, beleza deixa eu ir logo."

    "Chegando perto de uma das saídas da nave, *nome da IA* explica que a única forma de tampar o tanque é o selando por fora."

    "Pois a ruptura dele é externa, e Loren teria que colocar um traje e sair pela nave presa a um cabo para não sair voando e flutuar pelo espaço infinito."

    "Loren nunca imaginou que faria isso na sua vida e não estava preparada para aquilo, mas se era a única forma de conseguir se salvar ela faria sem nem pensar."

    "Colocou o traje e abriu aquela porta para enfim acabar com seu último empecilho, pegando uma nova cobertura para o tanque e seu fixador para prendê-lo, ela sai da nave."

    #troca pro exterior

    l "Certo *nome da IA* me guie até o tanque pra eu terminar isso logo."

    i "O tanque está no próximo setor, é só continuar seguindo essas barras de auxílio sem derrubar o tampo e você já vai estar lá."

    l "Certo!"

    "Nossa heroína chega ao tanque e se prepara para realizar seu último desafio."

    l "Achei a ruptura!"

    i "Muito bem senhorita, agora é só selar o buraco."

    l "Vamos nessa *nome da IA*."

    "Loren começa a colocar o tampo no buraco do tanque, ela pega o fixador em seu bolso, mas quando iria começar a fechar o tanque, o tampo escorrega de sua mão bate em seu capacete e abre uma brecha."

    "O oxigênio do traje começa a sair e não a mais nada que Loren possa fazer."

    "Ela já tinha aceitado que seu fim estava próximo, mas como uma última esperança, corta um pedaço de seu traje e faz uma isolação com sucesso no tanque e ele para de vazar."

    i "Senhorita rápido, volte imediatamente para a cabine não a tempo, ou a senhorita não irá sobreviver!"

    l "Não tem mais o que fazer *nome da IA*, eu tenho dois rompimentos no meu traje, o oxigênio vai acabar mais rápido do que eu chegar até a porta."

    i "Mas isso não é possível, por favor ten..."

    l "Eu já aceitei que vou morrer aqui neste lugar depois de ter salvado todos."

    l "Foi um bom fim."

    i "Senhorita, eu mostrarei a todos o que você fez, você não pode morrer em vão."

    l "{b}*Cof* *Cof*{/b} Obrigada *nome da IA* você me ajudou muito a não me fazer sentir sozinha nesse lugar."

    i "Eu que agradeço a você Senhorita Loren, algum último pedido?"

    #Escolha final

    menu:
        "Escolha Final"

        "Conte o que aconteceu para a tripulação":
            jump remember

        "Não conte":
            jump dont_remember

    return

label remember:

    scene black with fade

    "Com isso Loren diz suas últimas palavras, para que não importa o que aconteça, todos se lembrem de quem ela foi."

    l "De tudo, desculpe mãe, e de nada a todos vocês da nave."

    l "*Cof* *Cof* “Há, verdade, e pra não esquecer, se fodam Saul e Tina."

    l "E também, até mais e obrigados pelos peixes."

    return

label dont_remember:

    scene black with fade

    "lembraram de mim =)"

    return

label chapter4:

    call fade_music

    image b_central = im.Scale("images/bg ship_3.png", 1920, 1080)

    scene b_central with fade

    "Chegando perto de uma das saídas da nave, Aiden explica que a única forma de tampar o tanque é o selando por fora."

    "Pois a ruptura dele é externa, e Loren teria que colocar um traje e sair pela nave presa a um cabo para não sair voando e flutuar pelo espaço infinito."

    "Loren nunca imaginou que faria isso na sua vida e não estava preparada para aquilo, mas se era a única forma de conseguir se salvar ela faria sem nem pensar."

    play sound "sfxs/porta nave.ogg" volume 1.0

    "Colocou o traje e abriu aquela porta para enfim acabar com seu último empecilho, pegando uma nova cobertura para o tanque e seu fixador para prendê-lo, ela sai da nave."

    $ compress("ship", "bg ship_", 7)
    $ decompress("space")

    image b_space = im.Scale("images/bg space_0.png", 1920, 1080)

    scene b_space with fade

    play music "musics/ambiente espaço.ogg" fadein 1.0

    l "Certo Aiden me guie até o tanque pra eu terminar isso logo."

    i "O tanque está no próximo setor, é só continuar seguindo essas barras de auxílio sem derrubar o tampo e você já vai estar lá."

    l "Entendido!"

    "Loren chega ao tanque e se prepara para realizar seu último desafio."

    l "Achei a ruptura!"

    i "Muito bem senhorita, agora é só selar o buraco."

    l "Vamos nessa Aiden."

    call fade_music

    play music "musics/final creditos.ogg" fadein 1.0 volume 1.0

    $ compress("ship", "bg ship_", 7)

    # Começa o último puzzle

    jump puzzle4

    #"Loren começa a colocar o tampo no buraco do tanque, ela pega o fixador em seu bolso, mas quando iria começar a fechar o tanque, o tampo escorrega de sua mão bate em seu capacete e abre uma brecha."

    return

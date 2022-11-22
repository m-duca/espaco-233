label chapter1:

    scene black with fade
    call fade_music

    $ decompress("ship")

    image b_capsule = im.Scale("images/bg ship_0.png", 1920, 1080)

    pause 1.0

    play sound "sfxs/voice/laser.ogg" fadeout 0.0 volume 1.0
    pause 2.0

    scene b_capsule with fade

    play music "musics/tensao.ogg" fadein 1.0 volume 0.5

    i1 "Bem vinda a sua viagem espacial para o planeta Gilon, você deve estar se sentindo um pouco zonza no momento Loren, mas logo mais estará bem melhor."

    i1 "Só precisa se acostumar a voltar com 100\% do funcionamento do seu corpo."

    "Loren escuta a voz como se estivesse falando no seu ouvido enquanto começa a acordar de vez após todo o tempo em hibernação."

    "Ela finalmente acorda em seu quarto na nave, seus pertences estão todos guardados em seu armário e com isso recebe mais uma instrução."

    i1 "Por favor, após se arrumar dirija-se a sala de instruções, onde receberá uma pequena tutoria com os outros viajantes de seu setor para se prepararem para o resto de sua viagem."

    "Loren se prepara rapidamente e ansiosa por finalmente estar acordada, ela imagina tudo o que pode acontecer, as pessoas que vai conhecer, e toda a sua vida neste novo planeta que logo chamará de lar."

    call fade_music

    #começa gameplay, ir pra sala de instruções
    jump capsule_early

    return

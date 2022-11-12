label chapter1:
    # Cenas: CÁPSULA DA NAVE (bg firstchapter0)

    call fade_music

    scene black with fade
    # scene bg chapter1_0 with fade

    play music "musics/tensao.ogg" fadein 1.0

    i "Bem vinda a sua viagem espacial para o planeta Gilon, você deve estar se sentindo um pouco zonza no momento Loren, mas logo mais estará bem melhor."

    i "Só precisa se acostumar a voltar com 100\% do funcionamento do seu corpo."

    "Loren escuta a voz como se estivesse falando no seu ouvido enquanto começa a acordar de vez após todo o tempo em hibernação."

    "Ela finalmente acorda de verdade em seu quarto na nave, seus pertences estão todos guardados em seu armário e com isso ela recebe mais uma instrução."

    i "Por favor, após se arrumar dirija-se a sala de instruções, onde receberá uma pequena tutoria com os outros viajantes de seu setor para se prepararem para o resto de sua viagem."

    "Loren se prepara rapidamente e ansiosa por finalmente estar acordada, ela imagina tudo o que pode acontecer, as pessoas que vai conhecer, e toda a sua vida neste novo planeta que logo chamará de lar."

    scene black with fade
    # scene bg chapter1_0 with fade

    # "Ela sai de seu quarto e não vê ninguém, talvez todos de seu setor já tenham ido e só ela achando que estava bem adiantada está atrasada."

    # "Chegando na sala, está completamente sozinha, ela se sentia feliz pensando novamente estar adiantada e comemora levemente por sua \"conquista\"."

    #começa gameplay, ir pra sala de instruções

    jump chapter2

    return

label introduction:
    # Cenas: TERRA FUTURISTA (bg intro_0), PRÉDIO DA LASER (bg intro_1), CASA DA LOREN (bg intro_2), NAVE ESTACIONADA (bg intro_3)
    # CÁPSULA DA NAVE (bg intro_4)

    call fade_music

    scene black with fade
    # scene bg intro_0 with fade

    play music "musics/introducao.ogg" fadein 1.0

    "10 de julho de 2095, a era da mais alta tecnologia no mundo."

    "A vida na Terra chega a níveis completamente diferentes do que qualquer cientista poderia imaginar, mesmo com cálculos e predições realizadas, o futuro que ocorre nos dias presentes não é nada que ninguém pensou."

    "O planeta Terra de forma vasta e abrangente se tornou dois pólos de grande desastre, de um lado uma poluição enorme que diminui a capacidade de vida e outro com uma tecnologia muito avançada mas que causa grandes problemas econômicos."

    scene black with zoomin
    # scene bg intro_1 with zoomin

    "Laser, a maior detentora de monopólio e inovação da Terra cria novos projetos para o bem estar da civilização."

    "Como Marte já não é mais um sonho e sim uma antiga conquista, a gigante Laser define que o próximo passo para a humanidade seria a busca de novos locais para onde se ter um lar."

    "Muitas viagens interestelares vêm ao modo de transformar a vida dos seres humanos, contratando alguns com competências específicas."

    "Sendo assim, Loren aos seus 35 anos se oferece a uma viagem para um planeta observado com enormes capacidades de sobrevivência e expansão terrestre."

    "Ela decide que como sua vida na Terra já não parece mais ter objetivo, acredita que um novo começo em um novo planeta possa ser uma enorme possibilidade para ter algo melhor do que tinha antes."

    "Antes de viajar, Loren avisa sua irmã o que estava prestes a fazer."

    scene black with fade
    # scene bg intro_2 with fade

    t "Lo por favor me dei..."

    l "Eu não quero nenhuma explicação sua ou qualquer coisa que você queira me falar."

    t "Mas me desculpa eu não..."

    play sound "sfxs/voice/surpresa.ogg"
    l "Não quero ouvir Tina! Sério, só vim te avisar que eu estou indo embora, já me decidi e vou viajar."

    t "Como assim indo embora? Viajar pra onde Lo? O que você vai fazer?"

    l "Eu me inscrevi no programa da Laser e vou pra outro planeta começar uma nova vida!"

    t "O que? Por quê? Foi pelo o que eu fiz? Se for por favor Lo, mesmo assim não é algo que você precise se mudar pra outro planeta, viajar por anos e nunca mais ter a vida que têm aqui. Não faz isso por favor."

    play sound "sfxs/voice/risada.ogg"
    l "{b}*Gargalha*{/b} Não decidi ir me mudar pra casa do caralho simplesmente pelo o que aconteceu, eu realmente estou até bem, me sinto livre depois de tudo."

    l "Você pode continuar o que estava fazendo à vontade. Fala como se não parecesse verdade. Eu quero ter uma nova vida fora daqui, a viagem é daqui uma semana, só preciso terminar de enviar os documentos e fazer minhas malas."

    t "Então é isso, você nem vai ter um pingo de consideração pela sua irmã e simplesmente vai embora."

    l "Relaxa, a Laser vai te mandar um dinheiro por conta da minha falta, ajuda sua família com isso. Agora eu vou indo, tchau maninha."

    scene black with fade
    # scene bg intro_3 with fade

    "No dia da viagem, Loren está totalmente preparada, sem remorso algum ela entra na estação de lançamento, tudo já está quase pronto para a decolagem. Nisso ela é recebida por um dos trabalhadores da Laser."

    a "Bom dia, vai embarcar conosco hoje ou apenas veio para ver o lançamento na nave?"

    l "Oie, vim para embarcar mesmo, viajante número 233 direto para o planeta Gilon."

    a "A pois bem, me acompanhe por favor."

    play sound "sfxs/porta nave.ogg"
    pause 3.0

    scene black with fade
    # scene bg intro_4 with fade

    "Alguns minutos depois caminhando, o assistente a leva para a sala de preservação e redução de sentidos para uma criogenização perfeita, para que seja possível sua viagem sem parecer que envelheceu um ano sequer."

    "Ela passa por todos os procedimentos e antes de adormecer e ser mantida em sua câmara, o assistente a pergunta se tem mais alguma mensagem que ela gostaria de mandar ou falar com alguém."

    l "Eu gostaria de ligar para minha mãe."

    a "Certo."

    play sound "sfxs/telefone.ogg"
    "{b}*Toooo* *Toooo*{/b}"

    b "Alô?"

    l "Oi mãe, sou eu, a Lo."

    b "Oie minha filha, por que está me ligando a essa hora, aconteceu algo?"

    l "Nada mãe, eu só vim me despedir da senhora, estou indo viajar para muito longe e não irei mais ver você. {i}Diz já soluçando de tristeza e começa a chorar{/i}."

    b "Como assim filha, você veio me visitar ontem e não me falou nada disso."

    l "Sim eu sei mãe, eu só não queria preocupar a senhora, mas está tudo bem comigo, eu vou pra outro planeta ter uma nova vida está bem?"

    b "Filha, mas por que isso tão de repente e por que em outro planeta meu amor, eu nunca mais vou te ver?"

    l "Infelizmente mãe, quando eu acordar já vou estar em outro lugar, mas foi muito bom falar com você no meu último dia aqui na Terra."

    "Loren pede aos médicos que a façam dormir logo e não espera sua mãe terminar de falar."

    l "Eu te amo viu mãe, muito obrigado por você e o pai terem me criado da melhor forma que puderam."

    b "Não minha filha por favor não faça isso, eu te imploro volte para casa!"

    play sound "sfxs/voice/pensativa.ogg"
    l "Não da mais mãe... Eu já estou indo."

    play sound "sfxs/tecla 1.ogg"
    pause 1.0
    play sound "sfxs/tecla 2.ogg"

    "Loren começa a cair no sono escutando as últimas palavras de sua mãe e sentindo um pouco de arrependimento por estar ali, mas já não conseguia dizer mais nenhuma palavra pois a anestesia geral estava quase completa."

    "Nos últimos segundos consciente, Loren apenas escuta a voz de sua mãe a chamar."

    b "Eu te amo também minha filha volta pra ca...sa por...favor vol..."

    play sound "sfxs/motor ligando.ogg" fadein 1.0 fadeout 0.0
    "Dentro da nave nada mais acontece, sua viagem inicia, todos os passageiros estão adormecidos em suas cabines."

    "Para que dali 95 anos todos acordem esperando os últimos 5 anos de viagem interestelar para a chegada em sua nova casa."

    "Após a decolagem concluída os últimos tripulantes da nave se auto colocam para adormecerem, o capitão sendo o último, checa tudo antes de continuar com a viagem."

    play sound "sfxs/motor rodando.ogg" fadein 1.0 fadeout 0.0
    "Todos os parâmetros estão corretos, combustível necessário cheio e com tanques reservas carregados, tudo no seu devido lugar, traça a rota e está tudo como deveria estar, nada iria atrapalhar essa viagem."

    jump chapter1

    return

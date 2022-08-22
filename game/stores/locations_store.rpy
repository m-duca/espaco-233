init python in locations_store:

    #################################################################
    #                        DICIONÁRIOS                            #
    ################################################################

    # Armazenam as possibilidades de cada direção com base na localização atual
    # Coloque sempre na ordem em que aparecem no jogo

    # Dicionário da Direita
    possibilities_right = {
        "quarto" : "corredor",
        "corredor" : "banheiro",
        "sala" : "cozinha"
    }

    # Dicionário da Esquerda
    possibilities_left = {

    }

    # Dicionário de Cima
    possibilities_up = {

    }

    # Dicionário de Baixo
    possibilities_down = {

    }


    # Retorna a localização atual / label que está sendo executado
    def get_cur_location():
        return

    # Escolhendo a próxima label, passando o dicionário da direção  
    def switch_next(dictionary, cur_location):
        #return dict.get(get_cur_location(), "start")
        return dictionary.get(cur_location, "sala")

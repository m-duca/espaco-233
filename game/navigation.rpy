# Código da Navegação entre salas
init python:
    

    #################################################################
    #                        DICIONÁRIOS                            #
    ################################################################

    # Armazenam as possibilidades de cada direção com base na localização atual
    # Coloque sempre na ordem em que aparecem no jogo

    # Dicionário da Direita
    possibilities_right = {
        "start" : "corredor",
        "corredor" : "banheiro"
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

    # Armazeno a label que está sendo executada atualmente na variável current_label
    def label_callback(name, abnormal):
        store.current_label = name

    # Atualizo a label atual
    config.label_callback = label_callback

    # Dou jump para determinado Label
    def go_to_next(dictionary):
        renpy.jump(switch_next(dictionary))

    # Escolhendo a próxima label, passando o dicionário da direção  
    def switch_next(dictionary):
        #return dictionary.get(get_cur_location(), "start")
        return dictionary.get(current_label, "start")

    
#SCREENS REFERENTES AOS BOTÕES ABAIXO:

screen buttons_navigation:
    imagebutton:
        xpos 1543
        ypos 493
        xanchor 0
        yanchor 0
        idle "button1.png"
        hover "button2.png"
        action Jump(switch_next(possibilities_right))

    imagebutton:
        xpos 427
        ypos 493
        xanchor 0
        yanchor 0
        idle "button1.png"
        hover "button2.png"
        action Jump(switch_next(possibilities_right))
    

    

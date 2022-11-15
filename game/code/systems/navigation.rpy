# Código da Navegação entre salas
init python:

    #################################################################
    #                        DICIONÁRIOS                            #
    #################################################################

    # Armazenam as possibilidades de cada direção com base na localização atual
    # Coloque sempre na ordem em que aparecem no jogo

    # Dicionário da Direita
    possibilities_right = {
        "start" : "splashscreen",
        "corridor" : "capsule",
        "instruction_room" : "corridor",
        "central" : "instruction_room",
        "puzzle2" : "central"
    }

    # Dicionário da Esquerda
    possibilities_left = {
        "start" : "splashscreen",
        "corridor" : "instruction_room",
        "instruction_room" : "central",
        "central" : "puzzle2"
    }

    # Dicionário de Cima
    possibilities_up = {
        "start" : "splashscreen",
        "central" : "puzzle1",
        "puzzle3" : "central"

    }

    # Dicionário de Baixo
    possibilities_down = {
        "start" : "splashscreen",
        "capsule" : "corridor",
        "central" : "puzzle3",
        "puzzle1" : "central"
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
        return dictionary.get(current_label, "start")


# Screen dos botões de navegação

# Parametros:
# show_right, show_left, show_up e show_down ===> Mostrar os Botões
# pos_right, pos_left, pos_up, pos_down ===> Posições dos Botões

screen buttons_navigation (show_right, show_left, show_up, show_down):
    # Mostrar botão da direita
    if show_right:
        imagebutton:
            xpos 1768
            ypos 478
            xanchor 0
            yanchor 0
            idle "button_0.png"
            hover "button_4.png"
            action Jump(switch_next(possibilities_right))
    # Mostrar botão da esquerda

    if show_left:
        imagebutton:
            xpos 32
            ypos 478
            xanchor 0
            yanchor 0
            idle "button_1.png"
            hover "button_5.png"
            action Jump(switch_next(possibilities_left))

    # Mostrar botão de cima
    if show_up:
        imagebutton:
            xpos 898
            ypos 28
            xanchor 0
            yanchor 0
            idle "button_2.png"
            hover "button_6.png"
            action Jump(switch_next(possibilities_up))

    # Mostrar botão de baixo
    if show_down:
        imagebutton:
            xpos 898
            ypos 930
            xanchor 0
            yanchor 0
            idle "button_3.png"
            hover "button_7.png"
            action Jump(switch_next(possibilities_down))

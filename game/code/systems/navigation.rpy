# Código da Navegação entre salas
init python:

    #################################################################
    #                        DICIONÁRIOS                            #
    #################################################################

    # Armazenam as possibilidades de cada direção com base na localização atual
    # Coloque sempre na ordem em que aparecem no jogo

    # Dicionário da Direita
    possibilities_right = {
    "start" : "corredor",
    "corredor" : "banheiro"
    }

    # Dicionário da Esquerda
    possibilities_left = {
    "start" : "corredor",
    "corredor" : "banheiro"
    }

    # Dicionário de Cima
    possibilities_up = {
    "start" : "corredor",
    "corredor" : "banheiro"
    }

    # Dicionário de Baixo
    possibilities_down = {
    "start" : "corredor",
    "corredor" : "banheiro"
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

screen buttons_navigation (show_right, show_left, show_up, show_down, pos_right = Vector(),
    pos_left = Vector(), pos_up = Vector(), pos_down = Vector()):
    # Mostrar botão da direita
    if show_right:
        imagebutton:
            xpos pos_right.x
            ypos pos_right.y
            xanchor 0
            yanchor 0
            idle "button_0.png"
            action Jump(switch_next(possibilities_right))
    # Mostrar botão da esquerda

    if show_left:
        imagebutton:
            xpos pos_left.x
            ypos pos_left.y
            xanchor 0
            yanchor 0
            idle "button_1.png"
            action Jump(switch_next(possibilities_left))

    # Mostrar botão de cima
    if show_up:
        imagebutton:
            xpos pos_up.x
            ypos pos_up.y
            xanchor 0
            yanchor 0
            idle "button_2.png"
            action Jump(switch_next(possibilities_up))

    # Mostrar botão de baixo
    if show_down:
        imagebutton:
            xpos pos_down.x
            ypos pos_down.y
            xanchor 0
            yanchor 0
            idle "button_3.png"
            action Jump(switch_next(possibilities_down))

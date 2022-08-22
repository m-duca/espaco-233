
# Inicializando a Store goto
init python in goto_store:
    
    # Dicionário de possíveis localizações:
    rooms = {
            "one" : "one",
            "two" : "two",
            "three" : "three",
            "four" : "four"
    }

    # Função que retorna qual será a próxima sala
    def switch_room(cur_location):
        return rooms.get(cur_location, "one")


    # Verifico qual é minha localização atual
    # Movo para determinado Label

    # Função para dar jump para direita
    def go_to_right(cur_location):
        renpy.jump(switch_room(cur_location))
       
    # Função para dar jump para esquerda
    def go_to_left(cur_location):
        renpy.jump(switch_room(cur_location))

    # Função para dar jump para cima
    def go_to_up(cur_location):
        renpy.jump(switch_room(cur_location))

    # Função para dar jump para baixo
    def go_to_down(cur_location):
        renpy.jump(switch_room(cur_location))

################################################################
# TESTE
################################################################
label one:
    "FUI PARA DIREITA"
    return

label two:
    "FUI PARA ESQUERDA"
    return

label three:
    "FUI PARA CIMA"
    return

label four:
    "FUI PARA BAIXO"
    return

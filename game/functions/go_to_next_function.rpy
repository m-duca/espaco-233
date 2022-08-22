
# Criando e Inicializando a Função go_to_next
init python:

    # Dou jump para determinado Label
    def go_to_next():
        renpy.jump(locations_store.switch_next(locations_store.possibilities_right, "quarto"))

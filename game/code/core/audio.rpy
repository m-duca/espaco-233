
# Declaração e Inicialização de variáveis contendo SFX e Músicas

# SFX
# sempre declare a variável como "audio.nome"
define audio.glitch = "sfx/glitch.mp3"



# Música
# sempre declare a variável como "audio.nome"

# Volume Inicial do Jogo
label initial_volume:

    python:
        if not persistent.set_volumes:
            persistent.set_volumes = True

        if _preferences.volumes['music'] == 1 and _preferences.volumes['sfx'] == 1:

            try:
                _preferences.volumes['music'] = .50
                _preferences.volumes['sfx'] = .50
            except KeyError:
                _preferences.volumes['music'] = .50
                _preferences.volumes['sfx'] = .50

    return

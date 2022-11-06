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

# Efeito de transição entre as músicas
label fade_music:
    stop music fadeout 1.0
    return

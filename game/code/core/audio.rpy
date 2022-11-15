# Volume Inicial do Jogo
label initial_volume:

    python:
        if not persistent.set_volumes:
            persistent.set_volumes = True

        if _preferences.volumes['music'] == 1 and _preferences.volumes['sfx'] == 1:

            try:
                _preferences.volumes['music'] = 0.5
                _preferences.volumes['sfx'] = 0.75
            except KeyError:
                _preferences.volumes['music'] = 0.5
                _preferences.volumes['sfx'] = 0.75

    return

# Efeito de transição entre as músicas
label fade_music:

    stop music fadeout 1.0

    return

# SFX de passos
label steps:

    scene black with fade

    play sound "sfxs/passos metal.ogg" fadein 1.0 fadeout 0.0

    pause 2.0

    return

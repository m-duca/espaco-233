
# Declaração e Inicialização de variáveis contendo SFX e Músicas

# SFX
# sempre declare a variável como "audio.nome"
define audio.glitch = "sfx/glitch.mp3" 



# Música
# sempre declare a variável como "audio.nome"

# Volume Inicial do Jogo
label initial_volume:

    $ renpy.music.set_volume(0.75)
    $ renpy.sound.set_volume(0.75)

    return

define first_time_capsule = True

label capsule:

    if first_time_capsule == True:
        call fade_music
        play music "musics/ambiente nave.ogg"
        $ first_time_capsule = False
    else:
        call steps

    scene black with fade

    call screen buttons_navigation (False, False, False, True)

return

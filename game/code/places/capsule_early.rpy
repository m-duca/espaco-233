default first_time_capsule = True

label capsule_early:

    image b_capsule = "images/bg ship_0.png"

    if first_time_capsule == True:
        call fade_music

        play music "musics/ambiente nave.ogg"
        $ first_time_capsule = False


    else:
        call steps

    scene b_capsule with fade

    call screen buttons_navigation (False, False, False, True)

return

default first_time_capsule = True

label capsule_early:

    image b_capsule = im.Scale("images/bg ship_0.png", 1920, 1080)

    if first_time_capsule == True:
        call fade_music

        $ decompress("buttons")

        play music "musics/ambiente nave.ogg" volume 1.0
        $ first_time_capsule = False


    else:
        call steps

    scene b_capsule with fade

    call screen buttons_navigation (False, False, False, True)

return

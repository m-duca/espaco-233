define first_time_capsule = True

label capsule:
<<<<<<< HEAD

    if first_time_capsule == True:
        $ first_time_capsule = False
        call fade_music
        play music "musics/ambiente nave.ogg" fadein 1.0
    else:
        call steps

    call screen buttons_navigation (False, False, False, True)
=======
>>>>>>> parent of 1411a3b (Navigation update)

return

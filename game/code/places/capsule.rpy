label capsule:

    call steps

    image b_capsule = im.Scale("images/bg ship_0.png", 1920, 1080)

    scene b_capsule with fade

    call screen buttons_navigation (False, False, False, True)

return

label corridor_early:

    call steps

    image b_corridor = im.Scale("images/bg ship_1.png", 1920, 1080)

    scene b_corridor with fade

    call screen buttons_navigation (False, False, True, True)

return

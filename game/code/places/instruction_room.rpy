label instruction_room:

    call steps

    image b_instruction = im.Scale("images/bg ship_2.png", 1920, 1080)

    scene b_instruction with fade

    call screen buttons_navigation (True, True, False, False)

return

label instruction_room:

    call steps

    image b_instruction = "images/bg ship_2.png"

    scene b_instruction with fade

    call screen buttons_navigation (True, True, False, False)

return

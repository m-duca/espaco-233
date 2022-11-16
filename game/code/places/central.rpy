label central:

    if puzzle1_completed and puzzle2_completed and puzzle3_completed:
        jump chapter3

    call steps

    scene black with fade

    call screen buttons_navigation (True, True, True, True)

return

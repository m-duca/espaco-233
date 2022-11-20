default first_time_central = True

label central:

    if puzzle1_completed and puzzle2_completed and puzzle3_completed:
        jump chapter3

    if first_time_central == True:
        $ first_time_central = False
    else:
        call steps

    scene bgship_3 with fade

    call screen buttons_navigation (True, True, True, True)

return

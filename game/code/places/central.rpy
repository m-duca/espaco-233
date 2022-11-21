default first_time_central = True

label central:

    image b_central = "images/bg ship_3.png"

    if puzzle1_completed and puzzle2_completed and puzzle3_completed:
        jump chapter3

    if first_time_central == True:
        $ first_time_central = False
    else:
        call steps

    scene b_central with fade

    call screen buttons_navigation (True, True, True, True)

return

#jump é maiúsculo
screen doors_test:
    imagebutton:
        xpos 350 
        ypos 553
        idle "button1.png"
        hover "button2.png"
        action [endings = 1, Jump("end")]
    imagebutton:
        xpos 870
        ypos 553
        idle "button1.png"
        hover "button2.png"
        action [endings = 2, Jump("end")]
    imagebutton:
        xpos 1390 
        ypos 553
        idle "button1.png"
        hover "button2.png"
        action [endings = 3, Jump("end")]
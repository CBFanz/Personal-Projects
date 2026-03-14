rightmotor = 0
leftmotor = 0
leftirsensor = 0
rightirsensor = 0
pushbutton = False
while True:
    x = input("Which was is that bs deviating?").lower()
    if x == "left":
        leftirsensor = 0
        rightirsensor = 127
    elif x == "right":
        leftirsensor = 127
        rightirsensor = 0
    else:
        print("invalid bs going straight")
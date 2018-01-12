import time, random

from role import Role 

you = Role()

running = True
while running:
    
    action = input (">>")
    action = action.strip()
    if action == "hp":
        print (you.hp)
    elif action == "bag":
        you.bag.view()
    elif action == "exp":
        print (you.exp)
    elif action == "when":
        print ("[一月]已经是正午了，太阳躲在雾霾的后面，没有一点暖和的意思")  
    elif action == "bye":
        you.bye()
        running = False
    else:
        you.act(action)

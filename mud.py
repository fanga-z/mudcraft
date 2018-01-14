import time, random, weather

from role import Role 


you = Role()

running = True
while running:
    
    action = input (">>")
    action = action.strip()
    if action == "hp":
        print (you.hp)
    elif action == "bag":
        you.bag.view(you)
    elif action == "exp":
        print (you.exp)
    elif action == "when":
        info = weather.get_weather()
        if info != None:
            print (info['city'] + " PM2.5 " + str(info['data']['pm25']) + " 空气质量 " + info['data']['quality'] + " 温度 " + str(info['data']['wendu']) )
    elif action == "bye":
        you.bye()
        running = False
    else:
        you.act(action)

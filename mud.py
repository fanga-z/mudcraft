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
    elif action == "today":
        info = weather.get_weather()
        if info != None:
            print (info['city'], end=" ")
            print (info['data']['forecast'][0]['date'], info['data']['forecast'][0]['type'], end=" ")
            print (" PM2.5=" + str(info['data']['pm25']) ,  info['data']['quality'])
    elif action == "bye":
        you.bye()
        running = False
    else:
        you.act(action)

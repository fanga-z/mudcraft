import time, random
from pathlib import Path

class Director:
    def __init__(self):
        pass
    def enterScene(place):
         
        global current
      
        current = Scene(place)
        print (current.place)
        
    def nextScene(current, result):
  
        current.left()
        Director.enterScene(result)

class Role:
    def __init__(self):

        if Path("role.txt").exists():
            f = open("role.txt", "r" , encoding="UTF-8")
            self.exp = int(f.readline())
            self.hp = int(f.readline())
            self.name = f.readline().strip()
            self.place = f.readline().strip()
            print ("欢迎 {0:s} 回到游戏 EXP {1:d} HP {2:d}".format(self.name, self.exp, self.hp))
            f.close()
        else:
            self.name = input ("新来的，请输入你的名字:")
            self.exp = 0
            self.hp = 100
            self.place = "home.txt"
            print ("欢迎 {0:s} 进入游戏 EXP {1:d} HP {2:d}".format(self.name, self.exp, self.hp))
       
        Director.enterScene(self.place)
        
        
    def add_hp(self, hp):
        self.hp += hp
        print ("hp +", str(hp))
    def add_exp(self, exp):
        self.exp += exp
        print ("exp +", str(exp))
    def act(self, action, obj):
        print (obj.act(action, self))
    def bye(self):
        f = open("role.txt", "w" , encoding="UTF-8")
        f.write(str(self.exp) + "\n")
        f.write(str(self.hp) + "\n")
        f.write(self.name + "\n")
        f.write(current.file() + "\n")
        f.close()
        print ("档案已经保存, 再见")
        time.sleep(0.5)

class Scene:
    def __init__(self, file):
        f = open(file, "r" , encoding="UTF-8")
        self.place = f.readline().strip()
        self.fileTxt = file
        
        txt = f.readline().strip()
        actions = {}
        while not txt.startswith("go"):
            kv = txt.split(":")
            actions[kv[0].strip()] = kv[1].strip()
            txt = f.readline().strip()

        self.actions = actions
        
        
        txt = txt[3:]
        opt = txt.split(",")
        
        go_options = {}
        go_options_file = {}
        for i in opt:
            kv = i.split("#")
            go_options[kv[0].strip()] = kv[1].strip()
            go_options_file[kv[0].strip()] = kv[2].strip()
        self.go_options = go_options
        self.go_options_file = go_options_file
        f.close()
        
        
    def file(self):
        return self.fileTxt
    def where(self):
        return self.place    
    def left(self):
        pass
    def act(self, action, who):
        if action in self.actions.keys():
            who.add_exp(random.randint(1,10))
            return self.actions[action]
        else:
            return "please don't " + action

current = None
you = Role()

running = True
while running:
    
    action = input ("")
    if action == "hp":
        print (you.hp)
    elif action == "exp":
        print (you.exp)
    elif action == "when":
        print ("[一月]已经是正午了，太阳躲在雾霾的后面，没有一点暖和的意思")  
    elif action == "go":
        print (current.go_options)
        sel = input("请选择:"+ str(list(current.go_options.keys())))
        result = current.go_options_file[sel]
        time.sleep(1)
        Director.nextScene(current, result)  
    elif action == "bye":
        you.bye()
        running = False
    else:
        you.act(action, current)

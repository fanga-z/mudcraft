import time, random
from pathlib import Path

class Director:
    def __init__(self):
        pass
    def enterScene(place):
         
        global current
      
        current = Scene(place)
        print ("这里是" + current.place)
        
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
    def _punch(self, sel, target):
        
        if not sel in target.punch_options.keys():
            return
        
        value = target.punch_options[sel]
         
        punch_target = target.get_object(value)
        punch_target.react("punch", self)
        if punch_target.hp <= 0:
            target.remove_object(value)
            del target.punch_options[sel]
    def _go(self, sel, target):
        if not sel in target.go_options.keys():
            return
        result = target.go_options_file[sel]
        time.sleep(1)
        Director.nextScene(target, result)
    def act(self, action, target):
        if action.startswith("go"):
            arg = action.split(" ")
            if len(arg) == 2:
                self._go(arg[1], target)
            else:
                print (target.go_options)
                sel = input("请选择:"+ str(list(target.go_options.keys())))
                self._go(sel, target)
        elif action.startswith("punch"):
            arg = action.split(" ")
            
            if len(arg) == 2:
                self._punch(arg[1], target)
            else:    
                print (target.punch_options)
                sel = input("请选择:"+ str(list(target.punch_options.keys())))
                self._punch(sel, target)
        else:
            print (target.react(action, self))
   
        
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
        while not txt == "":
             
            if txt.startswith("go"):
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
            elif txt.startswith("punch"):
                txt = txt[6:]
                opt = txt.split(",")
                punch_options = {}
                for i in opt:
                    kv = i.split("#")
                    punch_options[kv[0].strip()] = kv[1].strip()
                    
                self.punch_options = punch_options
            else:
                kv = txt.split(":")
                actions[kv[0].strip()] = kv[1].strip()
            txt = f.readline().strip()

         
        self.actions = actions
        #场景里的物体 使用的时候自动创建
        self.objects = {}
        f.close()
        
    def get_object(self, value):
        if value in self.objects.keys():
            return self.objects[value]
        else:
            obj = Object(value)
            self.objects[value] = obj
            return obj
    def remove_object(self, value):
        if value in self.objects.keys():
            del self.objects[value]
            
    def file(self):
        return self.fileTxt
    def where(self):
        return self.place    
    def left(self):
        pass
    def react(self, action, who):
        if action in self.actions.keys():
            who.add_exp(random.randint(1,10))
            return self.actions[action]
        else:
            return "please don't " + action

class Object:
    def __init__(self, name):
        self.name = name
        self.hp = random.randint(3,6)
        self.reward = "武林秘籍"
    def react(self, action, who):
        if action == "punch":
            who.add_exp(random.randint(1,10))
            self.hp -= 1
            if self.hp == 0:
                print ("你赢了 得到" + self.reward)
            else:
                print ("你打了"+self.name + "一下 还得打"+str(self.hp)+"下")
        
        
current = None
you = Role()

running = True
while running:
    
    action = input (">>")
    action = action.strip()
    if action == "hp":
        print (you.hp)
    elif action == "exp":
        print (you.exp)
    elif action == "when":
        print ("[一月]已经是正午了，太阳躲在雾霾的后面，没有一点暖和的意思")  
    elif action == "bye":
        you.bye()
        running = False
    else:
        you.act(action, current)

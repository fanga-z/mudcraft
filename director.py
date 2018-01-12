import random
from objectdef import Object, ObjectDef

class Director:
    def __init__(self):
        pass
    def enterScene(place):
        current = Scene(place)
        print ("这里是" + current.place)
        return current
        
    def nextScene(current, next):
        current.left()
        return Director.enterScene(next)
 
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


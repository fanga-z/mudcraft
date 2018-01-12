import random

'''
物品的定义表
每个物品的名字HP和掉落物品
'''
class ObjectDef:
    def __init__(self):
        f = open("object_def.txt", "r" , encoding="UTF-8")
        txt = f.readline().strip()
        object_hp = {}
        object_get = {}
        while not txt == "":
            opt = txt.split(":")
            object_hp[opt[0]] = int(opt[1])
            object_get[opt[0]] = opt[2]
            txt = f.readline().strip()   
        self.object_hp = object_hp
        self.object_get = object_get
    def obj_hp_def(self, obj_name):
        if obj_name in self.object_hp.keys():
            return self.object_hp[obj_name];
        return 0
    def obj_get_def(self, obj_name):
        if obj_name in self.object_get.keys():
            return self.object_get[obj_name];
        return ""

 
objectDef = ObjectDef()

class Object:
    def __init__(self, name):
        self.name = name
        global objectDef;
        self.hp = objectDef.obj_hp_def(name);
        self.reward = objectDef.obj_get_def(name);
    def react(self, action, who):
        if action == "punch":
            who.add_exp(random.randint(1,10))
            self.hp -= 1
            if self.hp == 0:
                return self.reward
            else:
                print ("你打了"+self.name + "一下 还得打"+str(self.hp)+"下")
                return None

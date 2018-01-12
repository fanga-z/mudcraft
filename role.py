import time, random
from pathlib import Path
from director import Director
from bag import Bag

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
        self.scene = Director.enterScene(self.place)

        self.bag = Bag()
    def add_hp(self, hp):
        self.hp += hp
        print ("hp +", str(hp))
    def add_exp(self, exp):
        self.exp += exp
        print ("exp +", str(exp))
    def _punch(self, sel):
        
        if not sel in self.scene.punch_options.keys():
            return
        
        value = self.scene.punch_options[sel]
         
        punch_target = self.scene.get_object(value)
        reward = punch_target.react("punch", self)
        if reward != None:
            self.bag.add(reward, 1)
            print ("你赢了 得到" + reward)

        if punch_target.hp <= 0:
            self.scene.remove_object(value)
            del self.scene.punch_options[sel]
    def _go(self, sel):
        if not sel in self.scene.go_options.keys():
            return
        result = self.scene.go_options_file[sel]
        time.sleep(1)
        self.scene = Director.nextScene(self.scene, result)
    def act(self, action):
        if action.startswith("go"):
            arg = action.split(" ")
            if len(arg) == 2:
                self._go(arg[1])
            else:
                print (self.scene.go_options)
                sel = input("请选择:"+ str(list(self.scene.go_options.keys())))
                self._go(sel)
        elif action.startswith("punch"):
            arg = action.split(" ")
            
            if len(arg) == 2:
                self._punch(arg[1])
            else:    
                print (self.scene.punch_options)
                sel = input("请选择:"+ str(list(self.scene.punch_options.keys())))
                self._punch(sel)
        else:
            print (self.scene.react(action, self))
   
        
    def bye(self):
        f = open("role.txt", "w" , encoding="UTF-8")
        f.write(str(self.exp) + "\n")
        f.write(str(self.hp) + "\n")
        f.write(self.name + "\n")
        f.write(self.scene.file() + "\n")
        f.close()

        self.bag.save()
        print ("档案已经保存, 再见")
        time.sleep(0.5)

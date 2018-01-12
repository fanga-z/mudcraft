from pathlib import Path

import pickle

class Bag:
    def __init__(self):
        if Path("bag.pkl").exists():
            pickle_file = open("bag.pkl", 'br')
            self.bag = pickle.load(pickle_file)
            pickle_file.close()
        else:
            self.bag = {}    
    def add(self, obj, num):
        if obj in self.bag.keys():
            self.bag[obj] = self.bag[obj] + num
            if self.bag[obj] <= 0:
                del self.bag[obj]
        else:
            self.bag[obj] = num
    def save(self):
        pickle_file = open("bag.pkl", 'bw')
        pickle.dump(self.bag, pickle_file)
        pickle_file.close()
    def view(self):
        print (self.bag)
        response = input("你要使用什么物品吗?")
 
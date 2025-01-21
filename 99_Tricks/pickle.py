import pickle
import json

class Jan:
    def __init__(self,A,B):
        self.A=A
        self.B=B
    def printname(self):
        print(self.A,"->",self.B)

f=Jan(10,2)
f.printname()
f.B=100
f.printname()
with open('data.pickle','wb') as ok:
    pickle.dump(f,ok)


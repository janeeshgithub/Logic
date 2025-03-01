import Zzm1
class Janeesh:
    food="BURGER"
    juice="FROOTI"
    does="WORK"
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def eats(self):
        self.food="PIZZA"
        print(self.food)
    def drinks(self):
        self.juice="FIZZ"
        print(self.juice)
    @classmethod
    def classmet(cls):
        return cls.does
    @staticmethod
    def jane():
        print("NO CLASS OR OBJECT")

class VENKAT(Janeesh):
    def __init__(self):
        pass

class Outer:
    def __init__(self):
        self.e = "four"
        self.f = "five"
        self.g=Inner()

class Inner:
    def __init__(self):
        self.a = "one"
        self.b = "two"
        self.c = "three"

# Example Usage
outer_obj = Outer()
print(outer_obj.e)  # Output: 10
print(outer_obj.f)  # Output: 20
print(outer_obj.g.a)  # Output: 1
print(outer_obj.g.b)  # Output: 2
print(outer_obj.g.c)  # Output: 3

print('-'*30)

x=Janeesh("BTECH","CSBS")
print(Janeesh.classmet())
print(x.food)
x.eats()
print(x.food)
x.drinks()
Janeesh.jane()
VENKAT.jane()

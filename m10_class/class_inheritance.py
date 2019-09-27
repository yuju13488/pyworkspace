#繼承：新類別有共通屬性及方法。父類別superclass，子類別subclass。
class Animal():
    def __init__(self):
        print("Animal created")
    def whoAml(self):
        print("Animal")
    def eat(self):
        print("eating")

#繼承
class Dog(Animal): #繼承Animal
    def __init__(self):
        Animal.__init__(self) #使用父類別建構子
        print("Dog created")
    def whoAml(self): #改寫父類別內方法
        print("Dog")
    def bark(self): #擴充父類別所缺乏的方法
        print("woof")
d=Dog()
d.whoAml()
d.eat() #可使用父類別所定義的方法
d.bark()
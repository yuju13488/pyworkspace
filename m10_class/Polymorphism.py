class Dog:
    def run(self):
        print('Dog:run')
    def walk(self):
        print('Dog:walk')
class Cat:
    def run(self):
        print('Cat:run')
    def walk(self):
        print('Cat:walk')
class Horse:
    def run(self):
        print('Horse:run')
    def walk(self):
        print('Horse:walk')
def test(animal): #物件內的method名稱皆相同方可使用
    animal.run() #物件中皆有run
    animal.walk() #物件中皆有walk
def main():
    dog=Dog()
    cat=Cat()
    horse=Horse()
    test(dog) #將animal代換成dog
    test(cat) #將animal代換成cat
    test(horse) #將animal代換成horse
main()
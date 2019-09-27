#類別屬性
class Dog:
    species="哺乳動物" #類別屬性
    def __init__(self,breed,name):
        self.breed=breed
        self.name=name
jack=Dog("Lab","jack")
print(jack.name)
print(jack.species)
print(Dog.species) #類別屬性為公開，任何函式都能呼叫
class Animal:
    def __init__(self, type)->None:
        self.type = type

    def __str__(self) -> str:
        return f"Type = {self.type}:"

class Mammal(Animal):
    def __init__(self, type, info)->None:
        self.info="Mammals can give direct birth."
        super(Mammal, self).__init__(type)

    def __str__(self) -> str:
        return f"Type = {self.type}: Info: {self.info}:"

class WingedAnimal(Animal):
    def __init__(self, type)->None:
        self.can_fly = True
        super().__init__(type)
        
    def __str__(self) -> str:
        return f"Type = {self.type}: Can fly: {self.can_fly}:"

class Bat(Mammal, WingedAnimal):
    def __init__(self, type, info)->None:
        Mammal.__init__(self, type, info)
        WingedAnimal.__init__(self, type)
        self.nocturnal = True
        
    def __str__(self) -> str:
        return f"Type = {self.type}: Info: {self.info}: Nocturnal = {self.nocturnal}: Can fly={self.can_fly}"       

# create some objects of Bat class
bat = Bat("Bat", "Eats insects")
bird = WingedAnimal("Seagull")
dog=Mammal("dog", "domesticated")

print(bird)
print(dog)
print(bat)

# Polymorphism
#for my_obj in (bird, dog, bat):
#    print(my_obj)
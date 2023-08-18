class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise = noise
        self.health = 100
        self.energy = 100

    def sleep(self):
        print(f"{self.name} is sleeping. Health: {self.health}")
        self.health += 25
        print(f"New health: {self.health}")
        return self
    
    def eat(self):
        print(f"{self.name} is eating. Energy: {self.energy}. Health: {self.health}")
        self.energy += 5
        self.health += 10
        print(f"New energy: {self.energy}. New health: {self.health}.")
        return self

    def play(self):
        print(f"Playing with {self.name}, health: {self.health}")
        self.health += 5
        print(f"New health: {self.health}")
        return self
    
    def cry(self):
        print(f"{self.name} says: {self.noise}")



class Cat(Pet):
    # add in whatever is unique to this subclass
    def __init__(self, name, type, noise, stripes=False):
        # these are the requirements to construct the parent class, to constuct a pet
        super().__init__(name, type, None, noise)
        self.stripes = stripes
        self.health = 50
        self.energy = 20
    
    # how to pass in inherited methods
    def sleep(self):
        print(f"{self.name} is sleeping. Health: {self.health}")
        self.health += 30
        print(f"New health: {self.health}")
        return self
    
    #  you don't have to recreate functions that are already in the super
    # def eat(self):
    #     super().eat()
    #     return self
    
    def play(self):
        print(f"Playing with {self.name}, health: {self.health}")
        self.health += 10
        print(f"New health: {self.health}")
        return self
    
    # def cry(self):
    #     super.cry()
    #     return self
    


class Dog(Pet):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.health = 120
        self.energy = 50

    def sleep(self):
        super().sleep()
        return self
    
    def eat(self):
        super().eat()
        return self
    
    def play(self):
        print(f"Playing with {self.name}, health: {self.health}")
        self.health += 20
        print(f"New health: {self.health}")
        return self
    
    def cry(self):
        super().noise()
        return self
import Pet

class Ninja:
    # You are able to overwrite default parameters
    def __init__(self, first_name, last_name, pet=None, treats=None, pet_food=None):
        self.first_name = first_name
        self.last_name = last_name
        # pass in pet by name
        self.pet = pet
        # self.pet = None   You are unable to overwrite default attributes
        # multiple pets: self.pet = []
        self.treats = treats
        self.pet_food = pet_food

    # how to pass in a pet into user
    def walk(self):
        print(f"Walking {self.pet.name}.")
        self.pet.play()
        return self

    def feed(self):
        print(f"Feeding {self.pet.name}.")
        self.pet.eat()
        return self

    def bathe(self):
        print(f"Bathing {self.pet.name}.")
        self.pet.cry()
        return self

# inherited class is passed in this way
Banjo = Pet.Cat("Banjo", "Calico", "Mrrp")

Griffin = Ninja("Griffin", "Fore", Banjo, "Catnip", "Fancy feast")
print(Griffin.first_name)

Griffin.walk()
Griffin.feed()
Griffin.bathe()
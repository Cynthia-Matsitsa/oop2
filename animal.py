class Animal:
    def _init_(self,name):
        self.name = name
        
    def move(self):
        pass
    def make_noise(self):
        pass
    
class Cat(Animal):
    def move(self):
        print("The cat is walking")
    def make_noise(self):
        print("meow")
class Bird(Animal):
    def move(self):
        print("The bird is flying")
    def make_noise(self):
        print("chirp")        
class Fish(Animal):
    def move(self):
        print("The fish is swimming")
    def make_noise(self):
        print("Boops")
        

        
        
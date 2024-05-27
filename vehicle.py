class Vehicle:
    def _init_(self,model,make):
        self.model = model
        self.make = make
    def move(self):
        print("The vehicle is moving")
        
class Bus(Vehicle):
    def _init_(self,model,make,capacity):
        self.capaity = capacity
        
    def hoot(self):
        print("The bus is hooting")
    def check_capacity(self):
        print("The capacity is {self.capacity}")
        
        b=Bus("x","Isuzu",70)
        b.move()
        b.hoot()
        
        l=Lorry("T","mercecedes",1000)
        l.move()
        l.unload()
        
class Lorry(Vehicle):
    def _init_(self,model,make,load_weight):
         super()._init(model,make)
         self.load_weight=load_weight
    
    def unload(self):
        print("unloading the lorry")
                
            
    

    

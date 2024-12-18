#classes

class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    
    def moves(self):
        print("Move along..")
    
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")

my_car = Vehicle('Tesla','Model Y')

my_car.moves()
print(my_car.make)
print(my_car.model)
my_car.get_make_model()



your_car = Vehicle('Tata','Nexon')
your_car.get_make_model()
your_car.moves()

print("\n\n")
#Inheritance

class Airplane(Vehicle):
    def __init__(self, make, model,faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id
    def moves(self):
        print('Flies Along...')
    
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model} id {self.faa_id}")

    
class Truck(Vehicle):
    def moves(self):
        print('Rumbles Along')
    
class GolfCart(Vehicle):
    pass

cessna=Airplane('cessna','skyhawk','1200')
mack = Truck('mack','pinnacle')
golfwagon = GolfCart('Yamaha','GC100')

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()

#polymorphism
print("\n\n")

for v in (my_car,your_car,cessna,mack,golfwagon):
    v.get_make_model()
    v.moves()
    
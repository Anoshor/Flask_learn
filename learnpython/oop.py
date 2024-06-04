#string list are objects 
#__init__ is constructor -- default and parameterized constructors
#self (is a reference, can be named anything)== this.. that object or instance itself

class Car:
    color = "blue"
    brand = "Audi"
    features = ['cng']

    def __init__(self) -> None:
        pass

    def __init__(self, model) -> None:
        print("hola")
        self.model = model #model is attributes

    def carsound(self) -> str:
        return "brrr"

    #staticmethod -- class level method
    @staticmethod #deorator allows to wrap method without permanently modifying it -- change behavior just.. 
    def getwheels() -> int:
        return 4

car1 = Car("v8")
print((car1.model))
sound = car1.carsound()
print(sound)
wheels = car1.getwheels()
print(wheels)

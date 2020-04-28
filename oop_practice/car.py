
""" def accelerate(self):
        if self._is_engine_started == True:
            if self._current_speed < self._max_speed and self.nitro != 0:
                self._current_speed += self._acceleration
            #if self.nitro:
             #   self._current_speed += self._acceleration
                self._current_speed = math.ceil((self._current_speed)+(self._acceleration * 30)/100)
                self.nitro -= 10
            else:
                self._current_speed += self._acceleration
                if self._current_speed  >= self._max_speed:
                    self._current_speed = self._max_speed
                    self.nitro -= 10
        else:
            print("Start the engine to accelerate")
        
            
    def apply_brakes(self):
        if self._current_speed > self._tyre_friction:
            if self._current_speed >= (self._max_speed//2):
                self.nitro += 10
                self._current_speed -= self._tyre_friction
            else:
                self._current_speed -= self._tyre_friction
        else:
            self._current_speed=0   

def accelerate(self):
        if self._is_engine_started == True:
            if self._current_speed < self._max_speed  and self.nitro != 0:
                #self._current_speed += self._acceleration
                self.nitro -= 10
                self._current_speed += self._acceleration
                if self.nitro != 10 and self._current_speed >= (self._max_speed//2):
                    self._current_speed = math.ceil((self._current_speed)+(self._acceleration * 30)/100)
                    #self.nitro -= 10
            else:
                self._current_speed += self._acceleration
                if self._current_speed  >= self._max_speed:
                    self._current_speed = self._max_speed
                    self.nitro -= 10
        else:
            print("Start the engine to accelerate")
        
            
    def apply_brakes(self):
        if self._current_speed > self._tyre_friction:
            if self._current_speed >= (self._max_speed//2):
                self.nitro += 10
                self._current_speed -= self._tyre_friction
            else:
                #self.nitro += 10
                self._current_speed -= self._tyre_friction
        else:
            self._current_speed=0   """
"""
def accelerate(self):
        if self._is_engine_started == True:
            if self._current_speed < self._max_speed  and self.nitro != 0:
                #self._current_speed += self._acceleration
                self.nitro -= 10
                self._current_speed += self._acceleration
                if self.nitro != 10 and self._current_speed >= (self._max_speed//2):
                    self._current_speed = math.ceil((self._current_speed)+(self._acceleration * 30)/100)
                    #self.nitro -= 10
            else:
                self._current_speed += self._acceleration
                if self._current_speed  >= self._max_speed:
                    self._current_speed = self._max_speed
                    self.nitro -= 10
        else:
            print("Start the engine to accelerate")
        
            
    def apply_brakes(self):
        if self._current_speed > self._tyre_friction:
            if self._current_speed >= (self._max_speed//2):
                self.nitro += 10
                self._current_speed -= self._tyre_friction
            else:
                #self.nitro += 10
                self._current_speed -= self._tyre_friction
        else:
            self._current_speed=0   
            
            
    def accelerate(self):
        if self._is_engine_started == True:
            if self._current_speed >= self._max_speed:
                self._current_speed += self._acceleration
            if self._nitro:
                self._current_speed += self._acceleration
                self._current_speed = math.ceil((self._current_speed)+(self._acceleration * 30)/100)
                self._nitro -= 10
        else:
            self._current_speed = 0
            print("Start the engine to accelerate")
        
        if self._current_speed >= self._max_speed:
                self._current_speed = self._acceleration
"""

"""
class Truck:
    def __init__(self,color,max_speed,acceleration,tyre_friction,max_cargo_weight):
        
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.max_cargo_weight = max_cargo_weight
        self.load = 0
        self.curremt_speed = 0
        self.is_engine_started = False
    
    def load_cargo(self,loads_1):
        if self.is_engine_started == True:
            print("Cannot load cargo during motion")
        else:
            if self.max_cargo_weight < self.load + loads_1:
                print("Cannot load cargo more than max limit: {}".format(max_cargo_weight))
            else:
                self.load += loads_1
            
    
    def start_engine(self):
        self.is_engine_started = True
        
    def unload_cargo(self,loads_3):
        if self.is_engine_started == True:
            print("Cannot unload cargo during motion")
        else:
            self.load -= loads_3
    
    


if __name__ == "__main__":
    import json
    detail = json.loads(input())

    color = detail["color"]
    max_speed = float(detail["max_speed"])
    acceleration = float(detail["acceleration"])
    tyre_friction = float(detail["tyre_friction"])
    max_cargo_weight = float(detail["max_cargo_weight"])
    load_1, load_2, load_3 = [float(each) for each in detail["loads"]]

    truck = Truck(color=color, max_speed=max_speed, acceleration=acceleration,
                  tyre_friction=tyre_friction,
                  max_cargo_weight=max_cargo_weight)
    truck.load_cargo(load_1)
    print(truck.load)
    truck.start_engine()
    truck.load_cargo(load_2)

    truck.unload_cargo(load_3)


"""
class Car:
    def __init__(self, color,max_speed,acceleration,tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.current_speed = 0
        
    def start_engine(self):
        car.is_engine_started = True
           # pass
        
    def stop_engine(self):
        car.is_engine_started = False
        
        

if __name__ == "__main__":
    import json
    detail = json.loads(input())

    color = detail["color"]
    max_speed = float(detail["max_speed"])
    acceleration = float(detail["acceleration"])
    tyre_friction = float(detail["tyre_friction"])

    car = Car(color=color, max_speed=max_speed, acceleration=acceleration,
              tyre_friction=tyre_friction)

    car.start_engine()
    print(str(car.is_engine_started))
    car.stop_engine()
    print(str(car.is_engine_started))
    
    
"""

class Car:
    def __init__(self, color,max_speed,acceleration,tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.current_speed = 0
        
    def sound_horn(self):
        if self.current_speed == 0:
            print("Car not started yet")
        else:
            print("Beep Beep")
    
    def start_engine(self):
        self.current_speed += self.acceleration
            
        
    


if __name__ == "__main__":
    import json
    detail = json.loads(input())

    color = detail["color"]
    max_speed = float(detail["max_speed"])
    acceleration = float(detail["acceleration"])
    tyre_friction = float(detail["tyre_friction"])

    car = Car(color=color, max_speed=max_speed, acceleration=acceleration,
              tyre_friction=tyre_friction)
              
    

    car.sound_horn()
    car.start_engine()
    car.sound_horn()



""

class Car:
    def __init__(self, color,max_speed,acceleration,tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.current_speed = 0
        
    def start_engine(self):
        self.current_speed = self.acceleration
    
    def accelerate(self):
        self.current_speed = self.acceleration
        
    def apply_brakes(self):
        if self.current_speed > self.tyre_friction:
            self.current_speed -= self.tyre_friction
        else:
            self.current_speed=0
        


if __name__ == "__main__":
    import json
    detail = json.loads(input())

    color = detail["color"]
    max_speed = float(detail["max_speed"])
    acceleration = float(detail["acceleration"])
    tyre_friction = float(detail["tyre_friction"])

    car = Car(color=color, max_speed=max_speed, acceleration=acceleration,
              tyre_friction=tyre_friction)

    car.start_engine()
    car.accelerate()

    print(car.current_speed)
    car.apply_brakes()
    print(car.current_speed)
    car.apply_brakes()
    print(car.current_speed)
    car.apply_brakes()
    print(car.current_speed)
    car.apply_brakes()
    print(car.current_speed)
    
    
""
class Car:
    def __init__(self, color,max_speed,acceleration,tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.current_speed = 0
        
    def accelerate_speed1(self):
        self.current_speed = 0
        
    def start_engine(self):
        self.current_speed = 0
    
    def accelerate(self):
        self.current_speed += self.acceleration

if __name__ == "__main__":
    import json
    detail = json.loads(input())

    color = detail["color"]
    max_speed = float(detail["max_speed"])
    acceleration = float(detail["acceleration"])
    tyre_friction = float(detail["tyre_friction"])

    car = Car(color=color, max_speed=max_speed, acceleration=acceleration,
              tyre_friction=tyre_friction)


    car.accelerate_speed1()
    print(car.current_speed)
    car.start_engine()
    print(car.current_speed)
    car.accelerate()

    print(car.current_speed)
    car.accelerate()
    print(car.current_speed)

"""

#if self.max_speed < 0 or self.max_speed > 250:
             #   raise ValueError("Invalid value for max_speed ")
            #else:
            self.current_speed = self.acceleration
        

"""class Car:
    def __init__(self,color,accelerator):
        self.color = color
        self.accelerator = accelerator
        self.speed = 0
     if self.max_speed < 0:
            print("Invalid value for max_speed")
        else:
            self.max_speed = max_speed
           
    def accelerate(self):
        print("Speeding up!")
        self.speed += self.accelerator
        
    def apply_brakes(self):
        print("Applying Brakes")
        self.speed -= 10
"
""
>>> car = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3)
>>> car.sound_horn()
"Car not started yet"
>>> car.start_engine()
>>> car.sound_horn()
"Beep Beep"
""

#car_object.start_engine()
"print(car_object.tyre_friction)
print(car_object.color)
print(car_object.max_speed)
print(car_object.acceleration)
""
#print(car_object.is_engine_stared)
#car = Car("RED", 220, 10, 3)
#car.maximum_speed()
#car.start_engine()
#car.accelerate()
#car.apply_brakes()
#car.sound_horn()
#car.stop_engine()

"""
class Car:
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        self.color = color
        self.max_speed = max_speed
        if self.max_speed < 0 or self.max_speed > 250:
            raise ValueError("Invalid value for max_speed ")
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.is_engine_started = False
        self.current_speed = 0
        
    def start_engine(self):
        self.is_engine_started = True
        
    def accelerate(self):
        if self.is_engine_started == True and self.current_speed < self.max_speed:
            self.current_speed += self.acceleration
        else:
            print("Start the engine to accelerate")
            
    def apply_brakes(self):
        if self.current_speed > self.tyre_friction:
            self.current_speed -= self.tyre_friction
        else:
            self.current_speed=0
            
    def sound_horn(self):
        if self.is_engine_started == True:
            print("Beep Beep")
        else:
            print("Start the engine to sound_horn")
    
    def stop_engine(self):
        self.is_engine_started = False
         
        
"""



class Car:
    def __init__(self, color,max_speed,acceleration,tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.current_speed = 0
        
    def sound_horn(self):
        if self.current_speed == 0:
            print("Car not started yet")
        else:
            print("Beep Beep")
    
    def start_engine(self):
        self.current_speed += self.acceleration
            
        
    


if __name__ == "__main__":
    import json
    detail = json.loads(input())

    color = detail["color"]
    max_speed = float(detail["max_speed"])
    acceleration = float(detail["acceleration"])
    tyre_friction = float(detail["tyre_friction"])

    car = Car(color=color, max_speed=max_speed, acceleration=acceleration,
              tyre_friction=tyre_friction)
              
    

    car.sound_horn()
    car.start_engine()
    car.sound_horn()



""
class Car:
    def __init__(self, color,max_speed,acceleration,tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.current_speed = 0
        
    def start_engine(self):
        self.current_speed = self.acceleration
    
    def accelerate(self):
        self.current_speed = self.acceleration
        
    def apply_brakes(self):
        if self.current_speed > self.tyre_friction:
            self.current_speed -= self.tyre_friction
        else:
            self.current_speed=0
        


if __name__ == "__main__":
    import json
    detail = json.loads(input())

    color = detail["color"]
    max_speed = float(detail["max_speed"])
    acceleration = float(detail["acceleration"])
    tyre_friction = float(detail["tyre_friction"])

    car = Car(color=color, max_speed=max_speed, acceleration=acceleration,
              tyre_friction=tyre_friction)

    car.start_engine()
    car.accelerate()

    print(car.current_speed)
    car.apply_brakes()
    print(car.current_speed)
    car.apply_brakes()
    print(car.current_speed)
    car.apply_brakes()
    print(car.current_speed)
    car.apply_brakes()
    print(car.current_speed)
""

class BankAccount:
    def __init__(self, name,mobile_no):
        self.nme = name
        self.mob_no = mobile_no
        #self.acc_no = account_no
        self.generate_account_no()
        self.balance = 0
    def generate_account_no(self):
        import uuid
        self.acc_no = str(uuid.uuid4())
        
""
import math
class Fraction(object):
    def __init__(self,num,den):
        self._numerator = num
        self._denominator = den
        gcd_of_num = math.gcd(self._numerator,self._denominator)
        self._numerator //= gcd_of_num
        self._denominator //= gcd_of_num

        if self._denominator < 0:
            self._numerator = -(self._numerator)
            self._denominator = -(self._denominator)
        if self._numerator < 0 and self._denominator < 0:
            self._numerator = -(self._numerator)
            self._denominator = -(self._denominator)
     

    def __sub__(self,otherfraction):
        nume = self._numerator*otherfraction._denominator - self._denominator*otherfraction._numerator
        deno = self._denominator*otherfraction._denominator
        comm = math.gcd(nume,deno)
        newnum = nume//comm
        newden = deno//comm
        #print(newnum,newden)
        result = Fraction(newnum,newden)
        print(self,end = " - ")
        print(otherfraction,end = " = ")
        print(result)
        return result
            
    
    @property
    def numerator(self):
        return self._numerator
    @property
    def denominator(self):
        return self._denominator
        
    def  __str__(self):
        return (str(self._numerator)+'/'+str(self._denominator))



if __name__ == "__main__":
    import json

    input_args = list(json.loads(input()))

    fraction_one = Fraction(*input_args[0])
    fraction_two = Fraction(*input_args[1])

    result_fraction = fraction_one - fraction_two
    

    try:
        fraction_one._numerator
    except AttributeError:
        print("Missed protecting numerator")

    try:
        fraction_one._denominator
    except AttributeError:
        print("Missed protecting denominator")

    try:
        fraction_one.numerator = 1
        print("Missed setting safe access to numerator")
    except AttributeError:
        pass

    try:
        fraction_one.denominator = 1
        print("Missed setting safe access to numerator")
    except AttributeError:
        pass

    print(isinstance(fraction_one, Fraction))
    print(isinstance(fraction_two, Fraction))
    print(result_fraction.numerator)
    print(result_fraction.denominator)
    
    
    
"""
        
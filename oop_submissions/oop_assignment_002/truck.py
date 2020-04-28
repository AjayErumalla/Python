from car import Car
class Truck(Car):
    def __init__(self,color="Red", max_speed=0, acceleration=0, tyre_friction=0, max_cargo_weight=0):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self._max_cargo_weight = max_cargo_weight
        self._loads = 0
        
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
        
    @property
    def loads(self):
        return self._loads
            
    def load(self,cargo_weight):
        if self._current_speed == 0:
            if cargo_weight > 0:
                if self._loads + cargo_weight < self._max_cargo_weight:
                    self._loads += cargo_weight
                else:
                    print("Cannot load cargo more than max limit: {}".format(self._max_cargo_weight))
            else:
                raise ValueError("Invalid value for cargo_weight")
        else:
            print("Cannot load cargo during motion")
            
    def unload(self,cargo_weight):
        if cargo_weight < 0:
            raise ValueError("Invalid value for cargo_weight")
        if self._current_speed == 0:
            self._loads -= cargo_weight
        else:
            print("Cannot unload cargo during motion")
   
   
   
   
   
   
   
   
        
"""    def apply_brakes(self):
        if self._current_speed > self._tyre_friction:
            self._current_speed -= self._tyre_friction
        else:
            self._current_speed=0
            
    def stop_engine(self):
        self._is_engine_started = False
"""
        
"""
class Truck:
    def __init__(self,color="Red", max_speed=0, acceleration=0, tyre_friction=0, max_cargo_weight=0):
        self._color = color
        self._max_speed = max_speed
        self._acceleration = acceleration
        self._tyre_friction = tyre_friction
        self._max_cargo_weight = max_cargo_weight
        self._loads = 0
        self._current_speed = 0
        self._is_engine_started = False
        
        if max_speed < 0:
            raise ValueError("Invalid value for max_speed")
        
        if acceleration < 0:
            raise ValueError("Invalid value for acceleration")
        
        if tyre_friction < 0:
            raise ValueError("Invalid value for tyre_friction")
            
    @property
    def color(self):
        return self._color
        
    @property
    def max_speed(self):
        return self._max_speed
    
    @property
    def tyre_friction(self):
        return self._tyre_friction
        
    @property
    def acceleration(self):
        return self._acceleration
    
    @property
    def current_speed(self):
        return self._current_speed
        
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
        
    @property
    def loads(self):
        return self._loads
    
    @property
    def is_engine_started(self):
        return self._is_engine_started
   
    def start_engine(self):
        self._is_engine_started = True
        
    def accelerate(self):
        if self._is_engine_started == True:
            if self._current_speed < self._max_speed:
                self._current_speed += self._acceleration
                if self._current_speed  >= self._max_speed:
                    self._current_speed = self._max_speed
        else:
            print("Start the engine to accelerate")
            
    def sound_horn(self):
        if self._is_engine_started == True:
            print("Honk Honk")
        else:
            print("Start the engine to sound_horn")
            
    def load(self,cargo_weight):
        if self._current_speed == 0:
            if cargo_weight > 0:
                if self._loads + cargo_weight < self._max_cargo_weight:
                    self._loads += cargo_weight
                else:
                    print("Cannot load cargo more than max limit: {}".format(self._max_cargo_weight))
            else:
                raise ValueError("Invalid value for cargo_weight")
        else:
            print("Cannot load cargo during motion")
        
        
            
    def unload(self,cargo_weight):
        if cargo_weight < 0:
            raise ValueError("Invalid value for cargo_weight")
        if self._current_speed == 0:
            self._loads -= cargo_weight
        else:
            print("Cannot unload cargo during motion")
            
        
    def apply_brakes(self):
        if self._current_speed > self._tyre_friction:
            self._current_speed -= self._tyre_friction
        else:
            self._current_speed=0
            
    def stop_engine(self):
        self._is_engine_started = False
        
"""
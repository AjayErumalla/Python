class Deer:
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        self._age_in_months = age_in_months
        self._breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        
        if age_in_months > 1:
            raise ValueError("Invalid value for field age_in_months: {}".format(self._age_in_months))
        
        if required_food_in_kgs <= 0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(self._required_food_in_kgs))
        
    @property
    def age_in_months(self):
        return self._age_in_months
    
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    @property
    def breed(self):
        return self._breed
      
    def grow(self):
        self._required_food_in_kgs += 2
        self._age_in_months += 1
        
    @classmethod   
    def make_sound(cls):
        print("Buck Buck")
    
    @classmethod
    def breathe(cls):
        print("Breathe in air")
        
class Lion(Deer):
    def grow(self):
        self._required_food_in_kgs += 4
        self._age_in_months += 1
        
    @classmethod   
    def make_sound(cls):
        print("Roar Roar")
    
class Shark(Deer):
    def grow(self):
        self._required_food_in_kgs += 8
        self._age_in_months += 1
     
    @classmethod   
    def make_sound(cls):
        print("Shark Sound")
    
    @classmethod    
    def breathe(cls):
        print("Breathe oxygen from water")

class GoldFish(Shark):
    def grow(self):
        self._required_food_in_kgs += 0.2
        self._age_in_months += 1
     
    @classmethod   
    def make_sound(cls):
        print("Hum Hum")
        
class Zoo:
    def __init__(self,reserved_food_in_kgs = 0):
        self._animals_in_zoo=[]
        self._reserved_food_in_kgs = reserved_food_in_kgs
    
    @property
    def animals_in_zoo(self):
        return self._animals_in_zoo
        
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
        
    def add_food_to_reserve(self,quantity):
        self._reserved_food_in_kgs += quantity

    def add_animal(self,animal):
        self._animals_in_zoo.append(animal)
        
    def count_animals(self):
        return len(self._animals_in_zoo)
        
    def feed(self,consumed_food):
        if self._reserved_food_in_kgs > 0:
            food_feeded = consumed_food._required_food_in_kgs
            self._reserved_food_in_kgs -= food_feeded
            consumed_food.grow()
        
    def count_animals_in_given_zoos(self):
        return len(self._animals_in_zoo)

class Snake(Deer):
    @classmethod
    def make_sound(cls):
        print("Hiss Hiss")
        
    def grow(self):
        self._required_food_in_kgs += 0.5
        self._age_in_months += 1
        
   
zoo = Zoo()
gold_fish = GoldFish(age_in_months = 1, breed="Nemo", required_food_in_kgs=0.5)
zoo.add_animal(gold_fish)
lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
zoo.add_animal(lion)
deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
zoo.add_animal(deer)
#print(zoo.count_animals())
#print(zoo.animals_in_zoo)
    
        
        
        
        
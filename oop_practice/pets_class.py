class MakeSoundFlyRun:
    sound = ""
    running = ""
    flying = ""
    swimming = ""
    @classmethod
    def make_sound(cls):
        print(cls.sound)
    @classmethod
    def run(cls):
        print(cls.running)
    @classmethod
    def fly(cls):
        print(cls.flying)
    @classmethod
    def swim(cls):
        print(cls.swimming)
    
class Pokemon:
    def __init__(self,name,level=1):
        self._name = name
        self._level = level
        self._pikachu_attack = 0
        self._air_pikachu_attack = 0
        self._water_pikachu_attack = 0
        self._electric_pikachu_attack = 0
        
        if len(self._name) == 0:
            raise ValueError("name cannot be empty")
            
        if self._level <= 0:
            raise ValueError("level should be > 0")
            
    @property
    def name(self):
        return self._name
    @property
    def level(self):
        return self._level
            
class Pikachu(Pokemon,MakeSoundFlyRun):
    sound = "Pika Pika"
    running = "Pikachu running..."
    
    def __str__(self):
        return ("{} - Level {}".format(self._name,self._level))
    
    def attack(self):
        self._pikachu_attack = self._level * 10
        self._level += 1
        if self._level % 2 == 0:
            print("Electric attack with {} damage".format(self._pikachu_attack))
        else:
            print("Electric Attack with {} damage".format(self._pikachu_attack))

class Squirtle(MakeSoundFlyRun,Pokemon):
    sound = "Squirtle...Squirtle"
    running = "Squirtle running..."
    swimming = "Squirtle swimming..."
    
    def __str__(self):
        return ("{} - Level {}".format(self._name,self._level))
        
    def attack(self):
        self._pikachu_attack = self._level * 9
        self._level += 1
        if self._level % 2 == 0:
            print("Water attack with {} damage".format(self._pikachu_attack))
        else:
            print("Water Attack with {} damage".format(self._pikachu_attack))
            
class Pidgey(MakeSoundFlyRun,Pokemon):
    sound = "Pidgey...Pidgey"
    flying = "Pidgey flying..."
    
    def __str__(self):
        return ("{} - Level {}".format(self._name,self._level))
        
    def attack(self):
        self._pikachu_attack = self._level * 5
        self._level += 1
        if self._level % 2 == 0:
            print("Air attack with {} damage".format(self._pikachu_attack))
        else:
            print("Air Attack with {} damage".format(self._pikachu_attack))
        
class Swanna(MakeSoundFlyRun,Pokemon):
    sound = "Swanna...Swanna"
    flying = "Swanna flying..."
    swimming = "Swanna swimming..."
    
    def __str__(self):
        return ("{} - Level {}".format(self._name,self._level))
        
    def attack(self):
        self._air_pikachu_attack = self._level * 5
        self._water_pikachu_attack = self._level * 9
        self._level += 1
        #if self._level % 2 == 0:
        print("Water attack with {} damage".format(self._water_pikachu_attack))
        print("Air attack with {} damage".format(self._air_pikachu_attack))
    
class Zapdos(MakeSoundFlyRun,Pokemon):
    sound = "Zap...Zap"
    flying = "Zapdos flying..."
    
    def __str__(self):
        return ("{} - Level {}".format(self._name,self._level))
        
    def attack(self):
        self._air_pikachu_attack = self._level * 5
        self._electric_pikachu_attack = self._level * 10
        self._level += 1
        if self._level % 2 == 0:
            print("Electric attack with {} damage".format(self._electric_pikachu_attack))
            print("Air attack with {} damage".format(self._air_pikachu_attack))
        else:
            print("Electric Attack with {} damage".format(self._electric_pikachu_attack))
            print("Air attack with {} damage".format(self._air_pikachu_attack))
            
class Island:
    pokemon_count_list = []
    def __init__(self,name, max_no_of_pokemon, total_food_available_in_kgs):
        self._name = name
        self._max_no_of_pokemon = max_no_of_pokemon
        self._total_food_available_in_kgs = total_food_available_in_kgs
        self._pokemon_left_to_catch = 0
        self.pokemon_list = []
        
    @property
    def name(self):
        return self._name
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
        
    def __str__(self):
        return ("{} - {} pokemon - {} food".format(self._name,self._pokemon_left_to_catch,
        self._total_food_available_in_kgs))
        
    def add_pokemon(self,pokemon = 1):
        if self._pokemon_left_to_catch + pokemon <= self._max_no_of_pokemon:
            self._pokemon_left_to_catch += pokemon
        else:
            print("Island at its max pokemon capacity")
    
    # def add_pokemon(self,pokemon):
    #     self.pokemon_list.append(pokemon)
    #     self.pokemon_count_list.append(pokemon)
        
    # def count_poke(self,pokemon):
    #     count = 0
    #     for i in pokemon:
    #         count += len(i.pokemon_list)
    #     return count
    
    
class Trainer:
    def __init__(self,name):
        self._name = name
        self._experience = 100
        self._max_food_in_bag = 1000
        self._food_in_bag = 0
        
    @property
    def name(self):
        return self._name
        
    @property
    def experience(self):
        return self._experience
        
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
        
    @property
    def food_in_bag(self):
        return self._food_in_bag
        
    def __str__(self):
        return ("{}".format(self._name))

"""  96
class PokeMon:
    sound = ""
    def __init__(self,name = None,level = 1,master = None):
        self._name = name
        self._level = level
        self._master = None
    
        if len(self._name) == 0:
            raise ValueError("name cannot be empty")
            
        if self._level <= 0:
            raise ValueError("level should be > 0")
            
    def __str__(self):
        return f"{self._name} - Level {self._level}"

            
        
    @classmethod    
    def make_sound(cls):
        print(cls.sound)
        
    @property
    def name(self):
        return self._name
        
    @property
    def level(self):
        return self._level
    
    @property     
    def master(self):
        if self._master == None:
            print("No Master")
        else:
            return self._master
        
class running:
    by_run = ""
    @classmethod
    def run(cls):
        print(f"{cls.by_run} running...")
    

class swimming:
    by_swim = ""
    @classmethod
    def swim(cls):
        print(f"{cls.by_swim} swimming...")
        
        
class flying:
    by_fly = ""
    @classmethod
    def fly(cls):
        print(f"{cls.by_fly} flying...")


class Pikachu(PokeMon,running):
    sound = "Pika Pika"
    by_run = "Pikachu"
    
    def attack(self):
        print(f"Electric attack with {self.level*10} damage")
        
    
class Squirtle(PokeMon,running,swimming):
    sound = "Squirtle...Squirtle"
    by_run = "Squirtle"
    by_swim = "Squirtle"
    
    
    def attack(self):
        print(f"Water attack with {self.level*9} damage")
        
        
class Pidgey(PokeMon,flying):
    sound = "Pidgey...Pidgey"
    by_fly = "Pidgey"
    
    
    def attack(self):
        print(f"Air attack with {self.level*5} damage")
    
    
class Swanna(PokeMon,flying,swimming):
    sound = "Swanna...Swanna"
    by_fly = "Swanna"
    by_swim = "Swanna"
    
    
    def attack(self):
        print(f"Water attack with {self.level*9} damage")
        print(f"Air attack with {self.level*5} damage")
   
    
class Zapdos(PokeMon,flying):
    sound = "Zap...Zap"
    by_fly = "Zapdos"
    
    def attack(self):
        print(f"Electric attack with {self.level*10} damage")
        print(f"Air attack with {self.level*5} damage")
   


class Island:
    pokemon_list = []
    def __init__(self,name=None, max_no_of_pokemon=0, total_food_available_in_kgs=0):
        self._name = name
        self._max_no_of_pokemon = max_no_of_pokemon
        self._total_food_available_in_kgs = total_food_available_in_kgs
        self._pokemon_left_to_catch = 0
        self.pokemon_list.append(self)
        
    @property    
    def name(self):
        return self._name
        
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
        
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
        
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
        
    def __str__(self):
        return f"{self._name} - {self.pokemon_left_to_catch} pokemon - {self._total_food_available_in_kgs} food"

        
    def add_pokemon(self,pokemon):
        if self._pokemon_left_to_catch  == self._max_no_of_pokemon:
            print("Island at its max pokemon capacity")
            
        else:
            self._pokemon_left_to_catch += 1
            
            
    @classmethod     
    def get_all_islands(cls):
       return Island.pokemon_list
       
       
class Trainer(PokeMon,Island):
    def __init__(self,name):
        self._name = name
        self._experience = 100
        self._max_food_in_bag = 10*self._experience
        self._current_island = None 
        self._food_in_bag = 0
        self.list_pokemon = []
        
        
    def __str__(self):
        return f"{self._name}"
        
        
    @property
    def name(self):
        return self._name
        
    @property
    def experience(self):
        return self._experience
        
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
        
    @property
    def food_in_bag(self):
        return self._food_in_bag
    
    @property
    def current_island(self):
        if(self._current_island==None):
            print("You are not on any island")
        else:
            return self._current_island
    
    def move_to_island(self,island):
        self._current_island = island
            
    def collect_food(self):
        if self._current_island != None:
            if self.current_island._total_food_available_in_kgs > self._max_food_in_bag:
                if self._food_in_bag < self._max_food_in_bag:
                    self._food_in_bag += self._max_food_in_bag
                    self.current_island._total_food_available_in_kgs -= self._food_in_bag
                else:
                    self._food_in_bag = self._max_food_in_bag
            else:
                self._food_in_bag = self.current_island._total_food_available_in_kgs
                self.current_island._total_food_available_in_kgs = 0
                
        else:
            print("Move to an island to collect food")
            
  
    def catch(self,pokemon):
        pokemon._master = self
        self.list_pokemon.append(pokemon)
        if self._experience < pokemon.level*100:
            print(f"You need more experience to catch {pokemon.name}")
        else:
            print(f"You caught {pokemon.name}")
            self._experience += pokemon.level*20
            
      
    def get_my_pokemon(self):
        return self.list_pokemon
        
    

"""
class Pokemon:
    def __init__(self,name,level):
        self._name = name
        self._level = level
        self._pikachu_attack = 0
        
        if len(self._name) == 0:
            raise ValueError("name cannot be empty")
            
        if self._level <= 0:
            raise ValueError("level should be > 0")
            
    @property
    def name(self):
        return self._name
    @property
    def level(self):
        return self._level
        
class MakeSound(Pokemon):
    sound = ""
    @classmethod
    def make_sound(cls):
        print(cls.sound)
        
    def attack(self):
        self._pikachu_attack += 10
        self._level += 1
        print("Electric attack with {} damage".format(self._pikachu_attack))
        

            
class Pikachu(MakeSound):
    sound = "Pika Pika"
   # pikachu_attack = 0
    @classmethod
    def run(cls):
        print("Pikachu running...")
    
    # def attack(self):
    #     self._pikachu_attack += 10
    #     self._level += 1
    #     print("Electric attack with {} damage".format(self._pikachu_attack))
        


""""""""""""
class Animal:
    sound = "Buck Buck"
    food_increase = 12
    def __init__(self,age_in_months,breed,required_food_in_kgs):

        if age_in_months > 1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        else:
            self._age_in_months = age_in_months

        self._breed = breed

        if required_food_in_kgs > 0:
            self._required_food_in_kgs = required_food_in_kgs
        else:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))

    @property
    def age_in_months(self):
        return self._age_in_months

    @property
    def breed(self):
        return self._breed

    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs

    @classmethod
    def make_sound(cls):
        print(cls.sound)

    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += self.food_increase

class LandAnimals:
    @classmethod
    def breathe(cls):
        print("Breathe in air")

class WaterAnimals:
    @classmethod
    def breathe(cls):
        print("Breathe oxygen from water")

class HuntingAnimals:
    animal_sound = "Buck Buck"
    jantu = "No deers to hunt" 
    @classmethod
    def hunt(cls,zoo_objects):
        c = 0
        for i in zoo_objects.lists:
            if i.sound == cls.animal_sound:
                c = 1
                zoo_objects.lists.remove(i)
                break

        if c == 0:
            print(cls.jantu)

class Deer(Animal,LandAnimals):
    food_increase = 2
    sound = "Buck Buck"

class Lion(Animal,LandAnimals,HuntingAnimals):
    food_increase = 4
    sound = "Roar Roar"

class Shark(Animal,WaterAnimals,HuntingAnimals):
    food_increase = 8
    sound = "Shark Sound"
    animal_sound = "Hum Hum"
    jantu = "No GoldFish to hunt"

class GoldFish(Animal,WaterAnimals):
    food_increase = 0.2
    sound = "Hum Hum"

class Snake(Animal,LandAnimals,HuntingAnimals):
    food_increase = 0.5
    sound = "Hiss Hiss"

class Zoo:
    animals_count = []
    def __init__(self,reserved_food_in_kgs = 0):
        self._reserved_food_in_kgs = reserved_food_in_kgs
        self.lists = []

    @property    
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs

    def add_food_to_reserve(self,reserved_food):
        self._reserved_food_in_kgs += reserved_food

    def add_animal(self,animal):
        self.lists.append(animal)
        self.animals_count.append(animal)

    def count_animals(self):
        return len(self.lists)

    def feed(self,animal):
        if self._reserved_food_in_kgs > 0:
            self._reserved_food_in_kgs -= animal.required_food_in_kgs
            animal.grow()

    @classmethod
    def count_animals_in_all_zoos(cls):
       return len(cls.animals_count)

    @staticmethod
    def count_animals_in_given_zoos(zoo_objects):
        count = 0
        for i in zoo_objects:
            count += len(i.lists)
        return count
        
        
"""class Animals:
    sound = "" 
    feed = 0
    def __init__(self,age_in_months, breed, required_food_in_kgs):
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
        
    @classmethod
    def make_sound(cls):
        print(cls.sound)
        
    def grow(self):
        self._required_food_in_kgs += self.feed
        self._age_in_months += 1
        
class HuntAnimals:
    hunt_animal = 'Deer'
    hnt_animal = 'deers'
    def hunt(self,zoo):
        if zoo._new_animal_list[self.hunt_animal] == 0:
            print(f'No {self.hnt_animal} to hunt')
        else:
            #zoo.new_animal_list[self.hunt_animal] -= 1
            zoo.new_animal_list.pop(self.hunt_animal)
            zoo.animal_count -= 1

        
class LandAnimals:
    breaths = "Breathe in air"
    @classmethod
    def breathe(cls):
        print(cls.breaths)
        
class WaterAnimals:
    breaths = "Breathe oxygen from water"
    
    @classmethod
    def breathe(cls):
        print(cls.breaths)

class Deer(Animals,LandAnimals):
    sound = "Buck Buck"
    feed = 2
    name = "Deer"
    
class Lion(Animals,HuntAnimals,LandAnimals):
    sound = "Roar Roar"
    feed = 4
    name = "Lion"
    
class Shark(Animals,HuntAnimals,WaterAnimals):
    sound = "Shark Sound"
    feed = 8
    name = "Shark"
    hunt_animal = "GoldFish"
    hnt_aml = "GoldFish"

class GoldFish(Animals,WaterAnimals):
    sound = "Hum Hum"
    feed = 0.2
    name = "GoldFish"
    
class Zoo:
    count_animals_in_all = 0
    def __init__(self,reserved_food_in_kgs = 0):
        self._reserved_food_in_kgs = reserved_food_in_kgs
        self.animal_count = 0
        self._new_animal_list = {'Deer': 0,'Lion':0,'Shark':0,'GoldFish':0,'Snake':0}
        
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
       
    def add_food_to_reserve(self,quantity):
        self._reserved_food_in_kgs += quantity
        
    def add_animal(self,animal):
        self.animal_count += 1
        li = ['Lion','Shark','Snake','GoldFish','Deer']
        if str(animal.name) in li:
            self._new_animal_list[str(animal.name)] += 1
        Zoo.count_animals_in_all += 1
        
    def count_animals(self):
        return self.animal_count
        
    def feed(self,food_consumed):
        if self._reserved_food_in_kgs > 0:
            self._reserved_food_in_kgs -= food_consumed.required_food_in_kgs
            food_consumed.grow()
            
    @staticmethod        
    def count_animals_in_given_zoos(list):
        count = 0
        for i in list:
            count += i.animal_count
        return count
     
    @classmethod      
    def count_animals_in_all_zoos(cls):
        return Zoo.count_animals_in_all
    
    @property
    def new_animal_list(self):
        return self.new_animal_list
        
class Snake(Animals,HuntAnimals,LandAnimals):
    sound = "Hiss Hiss"
    feed = 0.5
    name = "Snake"

    

    
"""


""""""""""""""""
class Animals:
    sound = "Buck Buck"
    add_food = 2
    name = 'Deer'
    def __init__(self, breed, required_food_in_kgs,age_in_months=1):
        if age_in_months > 1:
            raise ValueError(f"Invalid value for field age_in_months: {age_in_months}")
        self._age_in_months = age_in_months
        self._breed = breed
        if required_food_in_kgs <= 0:
            raise ValueError(f"Invalid value for field required_food_in_kgs: {required_food_in_kgs}")
        self._required_food_in_kgs = required_food_in_kgs
        
    def __str__(self):
        return self.name
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += self.add_food
        
    @classmethod    
    def make_sound(cls):
        print(cls.sound)
        
    @property
    def age_in_months(self):
        return self._age_in_months
        
    @property
    def breed(self):
        return self._breed
        
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
 
class Carnivores:
    hunt_animal = 'Deer'
    h_animal = 'deers'
    def hunt(self,zoo):
        if zoo._animal_li[self.hunt_animal] == 0:
            print(f'No {self.h_animal} to hunt')
        else:
            zoo._animal_li[self.hunt_animal] -= 1
            zoo.animal_count -= 1
            
class LandAnimals:
    breath = "Breathe in air"
    @classmethod   
    def breathe(cls):
        print(cls.breath)
        
class WaterAnimals:
    breath = "Breathe oxygen from water"
    @classmethod   
    def breathe(cls):
        print(cls.breath)

class Deer(Animals,LandAnimals):
    pass

class Lion(Animals,Carnivores,LandAnimals):
    sound = "Roar Roar"
    add_food = 4
    name = 'Lion'
    
class Shark(Animals,Carnivores,WaterAnimals):
    sound = "Shark Sound"
    add_food = 8
    name = 'Shark'
    hunt_animal = 'GoldFish'
    h_animal = 'GoldFish'
    
class GoldFish(Animals,WaterAnimals):
    sound = "Hum Hum"
    add_food = 0.2
    name = 'GoldFish'
    
class Snake(Animals,Carnivores,LandAnimals):
    sound = "Hiss Hiss"
    add_food = 0.5
    name = 'Snake'
    
class Zoo():
    count_animals_in_all = 0
    def __init__(self):
        self._reserved_food_in_kgs = 0
        self.animal_count = 0
        self._animal_li = {'Deer': 0,'Lion':0,'Shark':0,'GoldFish':0,'Snake':0}
        
    def add_food_to_reserve(self,weight):
        self._reserved_food_in_kgs += weight
        
    def count_animals(self):
        return self.animal_count
        
    def add_animal(self,animal):
        self.animal_count += 1
        li = ['Lion','Shark','Snake','GoldFish','Deer']
        if str(animal) in li:
            self._animal_li[str(animal)] += 1
        Zoo.count_animals_in_all += 1
        
    def feed(self,animal):
        if self._reserved_food_in_kgs != 0:
            self._reserved_food_in_kgs -= animal.required_food_in_kgs
            animal.grow()
        
    @staticmethod
    def count_animals_in_given_zoos(list):
        count = 0
        for i in list:
            count += i.animal_count
        return count
        
    @classmethod
    def count_animals_in_all_zoos(cls):
        return Zoo.count_animals_in_all
        
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
        
    @property
    def animal_li(self):
        return self._animal_li
"""""""""""""""""""""""""""""
class Pets:

    #dogs = []

    def __init__(self, dogs):
        self.dogs = dogs
        #print(self.dogs)


class Dog:

    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True
        
    def eat(self):
        self.is_hungry = False
    
    def description(self):
        return self.name, self.age

    def speak(self, sound):
        return "%s says %s" % (self.name, sound)


class RussellTerrier(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)

class Bulldog(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)
        
class Streetdog(Dog):
    pass


my_dogs = [
    Bulldog("Tom", 6), 
    RussellTerrier("Fletcher", 7), 
    Dog("Larry", 9),
    Streetdog("jimmy",4)
]

my_pets = Pets(my_dogs)

print("I have {} dogs.".format(len(my_pets.dogs)))

for dog in my_pets.dogs:
    dog.eat()
    print("{} is {}.".format(dog.name, dog.age))

print("And they're all {}s, of course.".format(dog.species))

my_dogs_are_hungry = False
for dog in my_pets.dogs:
    if dog.is_hungry:
        my_dogs_are_hungry = True
        
if my_dogs_are_hungry:
    print("My dogs are hungry.")
else:
    print("My dogs are not hungry.")
        
    

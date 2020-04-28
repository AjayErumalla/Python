class MakeSoundFlyRunSwim:
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
    
class Attack:
    pass

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
            
class Pikachu(Pokemon,MakeSoundFlyRunSwim):
    sound = "Pika Pika"
    running = "Pikachu running..."
    
    def __str__(self):
        return ("{} - Level {}".format(self._name,self._level))
    
    def attack(self):
        self._pikachu_attack = self._level * 10
        self._level += 1
        print("Electric attack with {} damage".format(self._pikachu_attack))

class Squirtle(MakeSoundFlyRunSwim,Pokemon):
    sound = "Squirtle...Squirtle"
    running = "Squirtle running..."
    swimming = "Squirtle swimming..."
    
    def __str__(self):
        return ("{} - Level {}".format(self._name,self._level))
        
    def attack(self):
        self._pikachu_attack = self._level * 9
        self._level += 1
        print("Water attack with {} damage".format(self._pikachu_attack))
            
class Pidgey(MakeSoundFlyRunSwim,Pokemon):
    sound = "Pidgey...Pidgey"
    flying = "Pidgey flying..."
    
    def __str__(self):
        return ("{} - Level {}".format(self._name,self._level))
        
    def attack(self):
        self._pikachu_attack = self._level * 5
        self._level += 1
        print("Air attack with {} damage".format(self._pikachu_attack))
        
class Swanna(MakeSoundFlyRunSwim,Pokemon):
    sound = "Swanna...Swanna"
    flying = "Swanna flying..."
    swimming = "Swanna swimming..."
    
    def __str__(self):
        return ("{} - Level {}".format(self._name,self._level))
        
    def attack(self):
        self._air_pikachu_attack = self._level * 5
        self._water_pikachu_attack = self._level * 9
        self._level += 1
        print("Water attack with {} damage\nAir attack with {} damage".format(self._water_pikachu_attack,self._air_pikachu_attack))
    
class Zapdos(MakeSoundFlyRunSwim,Pokemon):
    sound = "Zap...Zap"
    flying = "Zapdos flying..."
    
    def __str__(self):
        return ("{} - Level {}".format(self._name,self._level))
        
    def attack(self):
        self._air_pikachu_attack = self._level * 5
        self._electric_pikachu_attack = self._level * 10
        self._level += 1
        print("Electric attack with {} damage\nAir attack with {} damage".format(self._electric_pikachu_attack,self._air_pikachu_attack))
            
class Island(Pokemon):
    pokemon_count = []
    def __init__(self,name,max_no_of_pokemon, total_food_available_in_kgs):
        self._name = name
        self._max_no_of_pokemon = max_no_of_pokemon
        self._total_food_available_in_kgs = total_food_available_in_kgs
        self._pokemon_left_to_catch = 0
        Island.pokemon_count.append(self)
        
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
        
    def add_pokemon(self,pokemon):
        if self._pokemon_left_to_catch < self._max_no_of_pokemon:
            self._pokemon_left_to_catch += 1
        else:
            print("Island at its max pokemon capacity")
            
    def __str__(self):
        return ("{} - {} pokemon - {} food".format(self._name,self._pokemon_left_to_catch,
        self._total_food_available_in_kgs))
            
    @classmethod       
    def get_all_islands(cls):
        return Island.pokemon_count
    

class Trainer(Island):
    def __init__(self,name):
        self._name = name
        self._experience = 100
        self._max_food_in_bag = 10 * self._experience
        self._food_in_bag = 0
        self._current_island = None
        
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
        if self._current_island == None:
            print("You are not on any island")
        else:
            return self._current_island
        
    def __str__(self):
        return ("{}".format(self._name))
        
    def move_to_island(self,island):
        self._current_island = island
       # return self._current_island
    
    def collect_food(self):
        pass
    
    def catch(self):
        pass
    
    def get_my_pokeman(self):
        pass
    
    
    
    
        
# def add_pokemon(self,pokemon):
    #     self.pokemon_list.append(pokemon)
    #     self.pokemon_count_list.append(pokemon)
        
    # def count_poke(self,pokemon):
    #     count = 0
    #     for i in pokemon:
    #         count += len(i.pokemon_list)
    #     return count
    
    
'''def __init__(self,age_in_months,breed,required_food_in_kgs):
        super().__init__(age_in_months,breed,required_food_in_kgs)'''
        

def __init__(self,reserved_food_in_kgs = 0):
        self._list_of_items=[]
        self._reserved_food_in_kgs = reserved_food_in_kgs
    
    @property
    def list_of_items(self):
        return self._list_of_items
        
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
        
    def add_food_to_reserve(self,quantity):
        self._reserved_food_in_kgs += quantity

    def add_animal(self,item):
        self._list_of_items.append(item)
        #print(item)
        
    def count_animals(self):
        return len(self._list_of_items)
        
    def feed(self,consumed_food):
        food_feeded = consumed_food._required_food_in_kgs
        self._reserved_food_in_kgs -= food_feeded
        #add_age = consumed_food._age_in_months
    
    
    
def hunt(self,animals_in_zoo):
        if animals_in_zoo.snake and animals_in_zoo.deer in animals_in_zoo:
            animals_in_zoo.remove(deer)
            print(animals_in_zoo)
        else:
            print("No deers to hunt")
            
            
"""

def __init__(self,age_in_months,breed,required_food_in_kgs,reserved_food_in_kgs = 0):
    #def __init__(self,age_in_months,breed,required_food_in_kgs,reserved_food_in_kgs = 0):
        #super().__init__(age_in_months,breed,required_food_in_kgs)
        self._list_of_items=[]
        self._reserved_food_in_kgs = reserved_food_in_kgs
        self._age_in_months = 
    
    @property
    def list_of_items(self):
        return self._list_of_items
        
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
        
    def add_food_to_reserve(self,quantity):
        self._reserved_food_in_kgs += quantity

    def add_animals(self,item):
        self._list_of_items.append(item)
        #print(item)
        
    def count_animals(self):
        return len(self._list_of_items)
        
    def feed(self,consumed_food):
        food_feeded = consumed_food._required_food_in_kgs
        self._reserved_food_in_kgs -= food_feeded
        self._age_in_months += 1
    
    
    
    

def filter(self,query):
        result = []
        
        for compare in self.list_of_items:
            
            key = getattr(compare,query.field)
            
            if (query.operation == 'IN' and key in query.value):
                result.append(compare)
                
            elif (query.operation == 'EQ' and key == query.value):
                result.append(compare)
                
            elif (query.operation == 'GT' and key > query.value):
                result.append(compare)
            
            elif (query.operation == 'GTE' and key >= query.value):
                result.append(compare)
                
            elif (query.operation == 'LT' and key < query.value):
                result.append(compare)
                
            elif (query.operation == 'LTE' and key <= query.value):
                result.append(compare)
                
            elif (query.operation == 'STARTS_WITH' and key.STARTS_WITH(query.value)):
                result.append(compare)
                
            elif (query.operation == 'ENDS_WITH' and key.ENDS_WITH(query.value)):
                result.append(compare)
            
            elif (query.operation == 'CONTAINS' and key.CONTAINS(query.value)):
                result.append(compare)
                
            #print(result)
                
        return "\n".join([str(x) for x in result])



store=Store()
item=Item(name="GoodDay Biscuit",price=30,category="Food")
result=store.add_item(item)
print(store)
"""


"""
if type(self.operation) != type(self.value):
            raise ValueError("Invalid value for query operation")
        else:
        
        
class Store(object):
    def __init__(self,name,price,category):
        super().__init__(name,price,category)
    def add_item(self,Item):
        items = [Item]
        Item.items_list.append(items)

"""

class Block:
    def __init__(self,block):
        self._value = block
        
    @property
    def value(self):
        return self._value
        
class SuperBlock(Block):
    def __init__(self,block):
        super().__init__(block)
        
    def split(self):
        if self._value > 1:
            if self._value % 2 == 0:
                return (SuperBlock(str(self._value // 2)), SuperBlock(str(self._value // 2)))
            elif self._value % 2 !=0:
                return (SuperBlock(str(int((self._value -1) / 2))), SuperBlock(str(int((self._value + 1) / 2))))
        else:
            return (SuperBlock(str(self._value)),)
            
    def __str__(self):
        top = "+"+"-"*len(str(self._value))+"+"+"\n"
        middle = '|'+str(self._value)+"|"+"\n"
        bottom = "+"+"-"*len(str(self._value))+'+'
        return (top + middle + bottom)

if __name__ == "__main__":
    super_block_value = int(input())

    super_block_one = SuperBlock(super_block_value)

    try:
        super_block_one._value
    except AttributeError:
        print("Missed protecting value")

    try:
        super_block_one.value = 1
        print("Missed setting safe access to value")
    except AttributeError:
        pass

    print(isinstance(super_block_one, SuperBlock))

    try:
        print(isinstance(super_block_one, Block))
    except:
        print("You should use Block class to build SuperBlock")

    blocks = super_block_one.split()
    if len(blocks) > 1:
        print(blocks[0])
        print(blocks[1])
    else:
        print(blocks[0])
        
        

class Block:
    def __init__(self, block):
        self._value=block
        
    @property
    def value(self):
        return self._value


class SuperBlock(Block):
    def __mul__(self,other):
        #if self.value == other.value:
        return Block(self.value*other.value)


if __name__ == "__main__":
    import json
    input_args = json.loads(input())

    super_block_one = SuperBlock(input_args[0])
    super_block_two = SuperBlock(input_args[1])

    try:
        super_block_one._value
    except AttributeError:
        print("Missed protecting value")

    try:
        super_block_one.value = 1
        print("Missed setting safe access to value")
    except AttributeError:
        pass

    print(isinstance(super_block_one, SuperBlock))

    print(isinstance(super_block_one, Block))

    product_block = super_block_one * super_block_two

    print(isinstance(product_block, Block))
    print(isinstance(product_block, SuperBlock))
    #print(product_block, SuperBlock)
    print(product_block.value)

    block_four = Block(4)

    try:
        block_four * product_block
        print("Multiplication is not supported on Block objects")
    except TypeError:
        pass





"""class person:
    def __init__(self,full_name):
        self.name = full_name
        
        
        #print("hello, i am {}".format(name))
        
    def say_hello(self):
        print("Hello I am {}".format(self.name)) 
        #print(self)
"       
    def greet(self, name="person"):
        return "Hello {}".format(name)
"
class Dog:

    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
        
        
        
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)




pinky = Dog("pinky",3)
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)
tinky = Dog('tinky',8)
rocky = Dog('rocky',7)

def get_biggest_number(*args):
    return max(args)
        #print(Dog.age)
"   
kim = Bulldog("kim",9)
print(kim.speak("bow bow"))
print()

kong = RussellTerrier("jane",10)
print(kong.description())

print(kong.run("faster"))

julie = Bulldog("Julie", 100)
print(isinstance(Bulldog, Dog))
"
johnnywalker = RussellTerrier("Johnny Walker", 4)
print(isinstance(johnnywalker, Bulldog))
    
print(get_biggest_number(pinky.age,philo.age,mikey.age,tinky.age,rocky.age))


print("{} is {} and {} is {}.".format(
    philo.name, philo.age, mikey.name, mikey.age))

if mikey.species == "mammal":
    print("{0} is a {1}!".format(mikey.name, mikey.species))
    
#print(isinstance(julie, jim))   

"

class Email:
    def __init__(self):
        self.is_sent = False
    def is_email_sent(self):
        self.is_sent = True
        
myemail = Email()
print(myemail.is_sent)

myemail.is_email_sent()
print(myemail.is_sent)
"
class Aa:
    pass
class Bb(Aa):
    pass


dd = Aa()
cc = Bb()

print(isinstance(dd,Bb))
"""

class Dog:
    species = 'mammal'

class SomeBreed(Dog):
    pass

class SomeOtherBreed(Dog):
    species = 'reptile'

frank = SomeBreed()
print(frank.species)

frank = SomeOtherBreed()
print(frank.species)



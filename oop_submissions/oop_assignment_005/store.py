class Item:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        if price < 1:
            raise ValueError("Invalid value for price, got {}" .format(self.price))
        self.category = category
 
    def __str__(self):
        return ("{}@{}-{}".format(self.name,self.price,self.category))

class Query:
    query_list = ['IN','EQ','GT','GTE','LT',"LTE",'STARTS_WITH','ENDS_WITH','CONTAINS']
    
    def __init__(self,field,operation,value):
        self.field = field
        self.operation = operation
        self.value = value
        
        if self.operation in self.query_list:
            pass
            #self.operation = operation
        else:
            raise ValueError("Invalid value for operation, got {}".format(self.operation))
        
    def __str__(self):
        return ("{} {} {}".format(self.field,self.operation,self.value))
    
class Store:
    
    def __init__(self):
        self.list_of_items=[]
        
    def __str__(self):
        if len(self.list_of_items)==0:
            return "No items"
        else:
            return "\n".join(map(str,self.list_of_items))
        
    def add_item(self,item):
        self.list_of_items.append(item)
        #print(item)
        
    def count(self):
        return len(self.list_of_items)
    
    def filter(self,query):
        filter_list = Store()
        
        for item in self.list_of_items:
           # print(item)
            key = getattr(item,query.field)
           # print(key)
            if (query.operation == 'IN' and key in query.value):
                filter_list.add_item(item)
                
            elif (query.operation == 'EQ' and key == query.value):
                filter_list.add_item(item)
                
            elif (query.operation == 'GT' and key > query.value):
                filter_list.add_item(item)
            
            elif (query.operation == 'GTE' and key >= query.value):
                filter_list.add_item(item)
                
            elif (query.operation == 'LT' and key < query.value):
                filter_list.add_item(item)
                
            elif (query.operation == 'LTE' and key <= query.value):
                filter_list.add_item(item)
                
            elif (query.operation == 'STARTS_WITH' and key.startswith(query.value)):
                filter_list.add_item(item)
                
            elif (query.operation == 'ENDS_WITH' and key.endswith(query.value)):
                filter_list.add_item(item)
            
            elif (query.operation == 'CONTAINS' and query.value in key):
                filter_list.add_item(item)
                
        #print(filter_list)
        return filter_list
    
    def exclude(self,query):
        exclude_list = Store()
        filter_query = self.filter(query)
        #print(filter_query)
        for item in self.list_of_items:
            #print(filter_query.list_of_items)
            if item not in filter_query.list_of_items:
                exclude_list.add_item(item)
        return exclude_list
"""        
store = Store()  
#item = Item(name="Oreo Biscuits", price=30, category="Food")  
store.add_item(item)  
#item = Item(name="Boost Biscuits", price=20, category="Food")  
store.add_item(item)  
#item = Item(name="ParleG Biscuits", price=10, category="Food")  
store.add_item(item) 
query = Query(field="price", operation="GT", value=15) 
#res = store.exclude(query)
#print(res)
print(store)  
"""
"""store = Store()  
item = Item(name="Oreo Biscuits", price=30, category="Food")  
store.add_item(item)  
item = Item(name="Boost Biscuits", price=20, category="Food")  
store.add_item(item)  
item = Item(name="Butter", price=10, category="Grocery")  
store.add_item(item)  
#query = Query(field="category", operation="IN", value=["Grocery"])
#results = store.filter(query)  
#print(results) 
query = Query(field="price", operation="GT", value=11)  
results = store.exclude(query)  
print(results)
#print(store)
"""
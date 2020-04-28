class Myclass:
    def method(self):
        return "Instance method is called"
        
    @classmethod
    def classmethod(cls):
        return "class method is called",cls
        
    @staticmethod
    def staticmethod():
        return "static method is called"
        
type_of_method = Myclass()
print(type_of_method.method())
#print(Myclass.method())

print(type_of_method.classmethod())
print(Myclass.classmethod())

print(type_of_method.staticmethod())
print(Myclass.staticmethod())
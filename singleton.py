


class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print("first time creating instance")
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
        
obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)  # This will print True, indicating both are the same instance
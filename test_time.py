from datetime import datetime

class BaseModel:
    def __init__(self):
        # retrive current local date and time
        self.created_at = datetime.now()
    
        # convert to string object in ISO format
        # self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        # convert to string object in ISO format using isoformat() method
        self.created_at = self.created_at.isoformat()
    def __init__(self, *args, **kwargs):
        # Loop and access all the values parsed into args
        if args:
            for values in args:
                print(values)
        # Loop and access all the key-value paired values parsed into kwargs
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        return "\n".join([f"{key}: {value}" for key, value in  self.__dict__.items()])

# parsing in multiple number of arguments
mod_1 = BaseModel("these", "are", "multiple", "number", "of", "args")

# parsing in multiple number of key-value paired arguments
mod_2 = BaseModel(name="Henok Haile", age="30")
print("\n=== outputs of kwargs below ===")
print(mod_2)
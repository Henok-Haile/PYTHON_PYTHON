from uuid import uuid4

class BaseModel:
    def __init__(self):
        self.id = str(uuid4())


mod_1 = BaseModel()
print(mod_1.id)

from enum import Enum

class Color(Enum):
    BLUE = 1
    YELLOW = 2
    RED = 3
    GREEN = 4
    

class Object:
    def __init__(self, object_id, size, color, bin0=None):
        self.object_id=object_id
        self.size=size
        self.color=color
        self.bin0=None
        pass

"""This is the base  class it manages the id attribute
"""


class Base:
    """declaring a private class attribute and initializing it with zero value"""
    __nb_objects = 0
    
    """Initializing  the Base class with an id attribute"""
    def __init__(self, id=None):
        """Assigning the public instance attribute id  with value id"""
        if id:
            self.id = id
        else:
           Base.__nb_objects += 1
           self.id = Base.__nb_objects
     
     
     
# b1 = Base()
# print(b1.id)
# b2 = Base()
# print(b2.id)
# b3 = Base()
# print(b3.id)
# b4 = Base(12)
# print(b4.id)
# b5 = Base()
# print(b5.id)
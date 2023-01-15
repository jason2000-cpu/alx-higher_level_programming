"""importing the Base class from base.py file."""


from base import Base


"""This class inherits from the Base class"""

class Rectangle(Base):
    """Initializing the Rectangle class with width, height, x, y and id attributes."""
    
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializing  the Rectangle class
        Args:
            width (int): The widht of the rectanle object
            height (int): The height of the rectangle object
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (int, optional): _description_. Defaults to None.
            
        """
        super().__init__(id)
        if isinstance(width, int):
            if width > 0:
                self.__width = width
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

        if isinstance(height, int):
            if height > 0:
                self.__height = height
            else:
                raise ValueError("height must be > 0")
        
        else:
            raise TypeError("height must be an integer")
        
        if isinstance(y, int):
            if y >= 0:
                self.__y = y
            else:
                raise ValueError ("y must be >= 0")
            
        else:
            raise TypeError("y must be an integer")
        
        if isinstance(x, int):
            if x >= 0:
                self.__x = x
            else:
                raise ValueError ("x must be >= 0")
        else:
            raise TypeError ("x must be an integer")
    
    def set_width(self, width):
        if isinstance(width, int):
            if width > 0:
                self.__width = width
            else:
                raise ValueError ("width must be > 0")
        else:
            raise TypeError ("width must be an integer")

    def get_width(self):
        return self.__width       
        
    
    
    def set_height(self, height):
        if isinstance(height, int):
            if height > 0:
                self.__height = height
            else:
                raise ValueError ("height must be > 0")
        
        else:
            raise TypeError ("height must be an integer")

    def get_height(self):
        return self.__height
        
        
    def set_y(self, y):
        if isinstance(y, int):
            if y >= 0:
                self.__y = y
            else:
                raise ValueError ("y must be >= 0")
            
        else:
            raise TypeError ("y must be an integer")

    def get_y(self):
        return self.__y
                

    def set_x(self, x):
        if isinstance(x, int):
            if self.__x >= 0:
                self.__x = x
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    def get_x(self):
        return self.__x
    
    def area(self):
        """calculates the area of the rectangle

        Returns:
            int: Returns the area of the rectangle
        """
        area = self.__width * self.__height
        return area
    
    def display(self):
        """
          This method prints in stdout the Rectangle instance
          with the character #
        """
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print("\b")
    
    
    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + str(self.id)+ ") "
        string += str(self.__x) + "/" + str(self.__y) + " - "
        string += str(self.__width) + "/" + str(self.__height)
        return string

    












"""tests"""



# """test 6"""

# """
#   Returns 
#   >>> [Rectangle] (12) 4/6
# """
# r1 = Rectangle(4, 6, 2, 1, 12)
# print(r1)


# """
#   Returns
#   >>> [Rectangle] (1) 1/0 - 5/5
# """
# r2 = Rectangle(5, 5, 1)
# print(r2)









# """test 5"""

# """
#  Returns 
#  >>> ####
#  >>> ####
#  >>> ####
#  >>> ####
#  >>> ####
#  >>> ####
# """
# r1 = Rectangle(4, 6)
# r1.display()

# print("----------------")

# """
#   Returns
#   >>> ##
#   >>> ##
# """
# r1 = Rectangle(2, 2)
# r1.display()

# """test 4"""

# """Returns >>> 6 """
# r1 = Rectangle(3, 2)
# print(r1.area())

# """Returns >>> 20 """
# r2 = Rectangle(2, 10)
# print(r2.area())

# """Returns >>> 56 """
# r3 = Rectangle(8, 7, 0, 0, 12)
# print(r3.area())






# """test 3"""

# """ Returns >>> [TypeError] height must be an integer """
# try:
#     Rectangle(10, "2")
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))


# """Returns >>> [ValueError] width must be > 0 """
# try:
#     r = Rectangle(10, 2)
#     r.set_width(-10) 
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))
    

# """Returns >>> [TypeError] x must be an integer """
# try:
#     r = Rectangle(10, 2)
#     r.set_x({})
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))

# """Returns >>> [ValueError] y must be >= 0"""
# try:
#     Rectangle(10, 2, 3, -1)
# except Exception as e:
#     print("[{}] {}".format(e.__class__.__name__, e))
    
    



# """test 2"""
# r1 = Rectangle(10, 2)
# print(r1.id)

# r2 = Rectangle(2, 10)
# print(r2.id)

# r3 = Rectangle(10, 2, 0, 0, 12)
# print(r3.get_height())






# """test 1"""   
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
class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    
    def set_width(self, value):
        if value <1:
            raise ValueError('Width cannot be less than 1.')
        else:
            self._width = value

    
    def set_height(self, value):
        if value < 1:
            raise ValueErroe('Height cannot be less than 1.')
        else:
            self._height = value

    
    def get_area(self):
        area = self._width * self._height
        return area

    
    def get_perimeter(self):
        perimeter = 2 * (self._width + self._height)
        return perimeter

    
    def get_diagonal(self):
        diagonal = ((self._width ** 2) + (self._height ** 2)) ** 0.5
        return diagonal

    
    def get_picture(self):
        picture = ''
        if self._height > 50 or self._width >50:
            return 'Too big for picture.'
        else:
            for i in range(self._height):
                picture += '*' * self._width +'\n' 
            return picture

    def get_amount_inside(self, shape):
        width_fit = self.width // shape.width
        height_fit = self.height // shape.height
        
        return width_fit * height_fit

    def __str__(self):
        return f'Rectangle(width={self._width}, height={self._height})'
class Square(Rectangle):
    def __init__(self, side):
        self._width  = side
        self._height = side
        self._side = self.set_side(side)

    def set_width(self, side):
        if side < 1:
            raise ValueError('Length cannot be less than 1.')
        else:
            self.set_side(side)


    def set_height(self, side):
        if side < 1:
            raise ValueError('Length cannot be less than 1.')
        else:
            self.set_side(side)

    def set_side(self, side):
        if side < 1:
            raise ValueError('Length cannot be less than 1.')
        else:
            self._width  = side
            self._height = side


    def __str__(self):
        return f'Square(side={self._width})'
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
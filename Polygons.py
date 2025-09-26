# Basic polygon classes and analysis, John Marsland last edited 9/26/25
class Rectangle:
    type = ''
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        if self.type == 'square':
            return f'Square(side={self.side_length})'
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width
        if self.type == 'square':
            self.side_length = width

    def set_height(self, height):
        self.height = height
        if self.type == 'square':
            self.side_length = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2*self.width + 2*self.height
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5
    
    def get_picture(self):
        picture = ''
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        for _ in range(self.height):
            picture += '*'*self.width + '\n'
        return picture

    def get_amount_inside(self, other):
        if other.height > self.height or other.width > self.width:
            return 0
        self_area = self.get_area()
        other_area = other.get_area()
        times_fit = self_area // other_area
        return times_fit

class Square(Rectangle):
    
    type = 'square'

    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        self.side_length = side_length

    def set_side(self, side_length):
        self.side_length = side_length
        self.height = side_length
        self.width = side_length



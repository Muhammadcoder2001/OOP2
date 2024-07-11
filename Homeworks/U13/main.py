'''U13:
Shape nomli Perent class berilgan va uning 4ta child classi bor.
1-class Line(chiziq), 
2-class Triangle(Uchburchak), 
3-class Rectangle(To'rtburchak)
4-class NullShape(bo'sh shakl). 
symbol va lenght propertysi bor.
Ularda show(), setSymbol(), setLength() degan metod bor.
Input:
L = Line(8)   
L.show()   
Output:
* * * * * * * *
Input:
T = Triangle()
T.show()

Output:
*
* *
* * *
* * * *
* * * * *
Input:
R = Rectangle(4)
R.setLength(6)
R.show()
Output:
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
Input:
S = NullShape(10)
S.show()
Output:
"Bo'sh shakl" degan yozuvchiqsin.'''

class Shape:
    def __init__(self, length, symbol):
        self.length = length
        self.symbol = symbol


    def set_symbol(self, new_symbol):
        self.symbol = new_symbol

    def set_length(self, new_length):
        self.length = new_length


class Triangle(Shape):
    def __init__(self, length = 5, symbol = " *"):
        super().__init__(length, symbol)


    def show(self):
        for i in range(1, self.length + 1):
            print(i * self.symbol)


class Line(Shape):
    def __init__(self, length = 8, symbol = " *" ):
        super().__init__(length, symbol)

    def show(self):
        print(self.symbol * self.length)


class Rectangular(Shape):
    def __init__(self, length = 6, symbol = " *"):
        super().__init__(length, symbol)
       

    def show(self):
        for i in range(1, self.length + 1):
            print(self.symbol * self.length)



class NUllShape(Shape):
    def __init__(self, length, symbol = ""):
        super().__init__(length, symbol)

    def show(self):
        print(f"Bo'sh Shakl!!!")

# s = NUllShape(100) 
# s.show()
# rec = Rectangular()
# rec.show()
# l1 = Line(8)
# l1.show()
# l1.set_symbol(" *")
# l1.set_length(12)
# l1.show()

# tri = Triangle(" *", 5)
# tri.show()
# tri.set_length(6)
# tri.set_symbol(" []")
# tri.show()

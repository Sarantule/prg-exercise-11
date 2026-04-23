#
import random
def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]



#
values = random_numbers(10)  # 10 čísel v rozsahu 0–100
print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20



#
my_list = [3, 8, 1, 2, 32]
my_list.sort()
print(my_list)   # [1, 2, 3, 8, 32]



#
my_list = [3, 8, 1, 2, 32]
new_list = sorted(my_list)
print(my_list)   # [3, 8, 1, 2, 32]   ← beze změny
print(new_list)  # [1, 2, 3, 8, 32]



#
my_list = [3, 8, 1, 2, 32]
my_list = sorted(my_list, reverse=True)
print(my_list)   # [32, 8, 3, 2, 1]



#
list_of_words = ["MOO", "meeeoow", "woof", "BZZZZZZ"]
list_of_words = sorted(list_of_words, key=len)
print(list_of_words)   # ['MOO', 'woof', 'meeeoow', 'BZZZZZZ']



#
list_of_words = ["MOO", "meeeoow", "woof", "BZZZZZZ"]
list_of_words = sorted(list_of_words, key=str.lower)



#
text = "acgt"
text.upper()          # metoda upper() na objektu třídy str — vrátí "ACGT"
numbers = [1, 2, 3]
numbers.append(4)     # metoda append() na objektu třídy list — rozšíří seznam na [1, 2, 3, 4]



#
width_1 = 3
height_1 = 5
width_2 = 10
height_2 = 20
width_3 = 1
height_3 = 1

def area(width, height):
    return width * height

def perimeter(width, height):
    return 2 * (width + height)

def fencing_cost(width, height, price_per_meter):
    return perimeter(width, height) * price_per_meter

print(area(width_1, height_1))                 # 15
print(perimeter(width_2, height_2))            # 60
print(fencing_cost(width_3, height_3, 250))    # 1000



#
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def fencing_cost(self, price_per_meter):
        return self.perimeter() * price_per_meter



#
r1 = Rectangle(3, 5)
r2 = Rectangle(10, 20)
r3 = Rectangle(1, 1)
print(r1.area())              # 15
print(r2.perimeter())         # 60
print(r3.fencing_cost(250))   # 1000



#
rectangles = [
    Rectangle(3, 5),
    Rectangle(10, 20),
    Rectangle(1, 1),
    Rectangle(7, 2),
    Rectangle(4, 8),
]

for rect in rectangles:
    print(rect.area())



#
r = Rectangle(3, 5)



#
small_rect = Rectangle(2, 3)
big_rect = Rectangle(10, 20)
print(small_rect.area())   # 6
print(big_rect.area())     # 200
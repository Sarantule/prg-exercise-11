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
import random

# print("Statement 1")
# print("Statement 2")
# print("Statement 3")
# print("Statement 4")
# print("Statement 5")
# print("Statement 6")
# print("Statement 7")
# print("Statement 8")

from src.operations_with_two import add_two, subtract_two, multiply_by_two, divide_by_two

def roll_dice(times_to_roll):
    x = []
    for i in range(1, times_to_roll + 1):
        x.append(random.randint(1, 6))
    return x

print(roll_dice(5))
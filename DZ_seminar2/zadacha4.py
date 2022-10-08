#Реализуйте алгоритм перемешивания списка.

import random
list = [random.randint(0,10) for i in range(random.randint(3,7))]
print(f"Исходный список:\n{list}")
random.shuffle(list)
print(f"Список после перемешивания:\n{list}")



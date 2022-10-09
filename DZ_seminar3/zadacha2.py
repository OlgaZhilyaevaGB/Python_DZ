#Напишите программу, которая найдёт произведение пар чисел списка (Cписок создаем как в предыдущем задании). 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#*Пример:*

#[2, 3, 4, 5, 6] => [12, 15, 16];
#[2, 3, 5, 6] => [12, 15]

num = int(input('Введите размер списка: '))
list = []
list2=[]
for i in range(num):
   list_number = int(input(f'Введите число {i+1}: '))
   list.append(list_number)
print(list)

for i in range(len(list)):
    while i < len(list)/2 and num > len(list)/2:
        num = num - 1
        a = list[i] * list[num]
        list2.append(a)
        i += 1
print(list2)
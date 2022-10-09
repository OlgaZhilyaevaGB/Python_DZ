#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
#ВАЖНО: если число целое, то оно не имеет дробной части и засчитывать 0 как минимальное не стоит
#Пример:

#[1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform
n = int(input('Введите размер списка '))
list1 = []
for i in range(n):
    a = uniform(0, 9)
    list1.append(round(a, 2))
print(list1)

list2=[]
for i in list1:
    b=i%1
    list2.append(round(b,2))
for i in list2:
    if i==0:
       list2.pop(i)

min = list2[0]
max=0
for i in range(len(list2)):  
    if max < (list2[i]):
       max = list2[i]     
    if min > (list2[i]):
       min = list2[i]       
raz = (max-min)
print(round(raz,2))

#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от-100 до 100)
#многочлена и записать в файл многочлен степени k
#k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
#Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

#Пример:
#k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
#k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

from random import randint as r

def list1():
    stepen=int(input('Введите натуральную степень: '))
    rez=''
    for i in range(stepen,-1,-1):
        num=r(-20,20)
        if i==stepen:
            if num>0:
                rez+=str(num) + 'x**' + str(i)
            if num<0:    
                rez+=' - '+str(abs(num))+'x**'+str(i)
        else:
            if num>0:
              rez+=' + '+str(num)+'x**'+str(i)
            if num<0:    
              rez+=' - '+str(abs(num))+'x**'+str(i)
    return rez

st1 = list1()
print(f"{(st1.replace('x**1','x').replace('x**0','')).replace('1x**','x')}=0")
st2 = list1()
print(f"{(st2.replace('x**1','x').replace('x**0','')).replace('1x**','x')}=0")
#Даны два файла, в каждом из которых находится запись многочлена.
#Задача - сформировать файл, содержащий сумму многочленов.

#Пример двух заданных многочленов:
#23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
#17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0
#Результат:
#40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0
pathWrite=r"homework\DZ_seminar4\file1.txt"
pathWritesum=r"homework\DZ_seminar4\filesum.txt"
pathWrite1=r"homework\DZ_seminar4\file2.txt"
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

firstYr=list1()
one=firstYr
secondYr=list1()
two=secondYr
firstYr=firstYr.replace(" + "," +").replace(' - ',' -').split()
secondYr=secondYr.replace(' + ',' +').replace(' - ',' -').split()

def createSlovar(first):
    slovar={}
    for i in range(len(first)):
        first[i]=first[i].replace("+","").split("x**")
        slovar[int(first[i][1])]=int(first[i][0])
    return slovar

word=createSlovar(firstYr)
word2=createSlovar(secondYr)
finalWord={}
for i in range(max(len(word),len(word2)),-1,-1):
    first=word.get(i)
    second=word2.get(i)
    if first!=None or second !=None:
        finalWord[i]=(first if first!=None else 0)+(second if second != None else 0)
print(finalWord)

try:
    with open(pathWritesum,'w') as data:
        data.write(str(finalWord))
        data.write('\n')
except:
    print("файл не найден")     

try:
    with open(pathWrite,'w') as data:
        data.write(str(one))
        data.write('\n')
except:
    print("файл не найден")    
try:
    with open(pathWrite1,'w') as data:
        data.write(str(two))
        data.write('\n')
except:
    print("файл не найден")    


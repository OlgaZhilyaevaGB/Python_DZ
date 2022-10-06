#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

flag=True
for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            if not(x or y or z)!=(not x and not y and not z):
                print("Выражение не верно")
                flag=False
    break
if flag:
     print("Выражение верно")       


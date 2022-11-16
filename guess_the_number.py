#guess the number РАБОЧАЯ ВЕРСИЯ БЕЗ ОГРАНИЧЕНИЙ ПО ДИАПАЗОНУ
import numpy as np
n = 100
number = np.random.randint(1, n+1) # загадываем число
#number = 100
count=1
predict_number=n/2
if number>50:
    nd=50
    kd=101
if number<50:
    nd=0
    kd=50
while True:
    if predict_number==number:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break  
    while predict_number<number:
        ub=predict_number
        predict_number=(nd+kd)//2
        nd=predict_number
        count +=1
        if predict_number>number:
            nd=ub
            kd=predict_number
            break
    while predict_number>number:
        ub=predict_number
        predict_number=(nd+kd)//2
        kd=predict_number
        count +=1
        if predict_number<number:
            nd=predict_number
            kd=ub
            break
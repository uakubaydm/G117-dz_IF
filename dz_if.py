# -*- coding: utf-8 -*-
a = int(input("Введите число А:"))
b = int(input("Введите число Б:"))
v = int(input("Введите число В:"))
if a < b:
    print("Да ну!")
elif a > b:
    print ("Свершилось!")
else:
    print("А если так? Прибавим к А В, а от Б отнимем В и заново сравним")

    a += v
    b -= v
    if a < b:
        print("Да ну!")
    else:
        print ("Свершилось!")
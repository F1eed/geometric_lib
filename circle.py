import math #импортируем модуль math для получения константы PI


def area(r): #функция area(r) принимает один аргумент(радиус), возвращает площадь окружности с данным радиусом
        #area(r) -> int
        return math.pi * r * r # area(2) -> ~(4*3,1415)


def perimeter(r): #функция perimeter(r) принимает один аргумент(радиус), возвращает длину окружности
        #perimeter(r) -> int
        return 2 * math.pi * r #perimeter(6) -> ~(12*3,1415) 


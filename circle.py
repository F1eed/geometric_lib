import math

def area(r): 
        '''
        Функция area(r) принимает один аргумент(радиус), возвращает площадь окружности с данным радиусом
                Параметры:
                        r(int)
                        
                Возвращаемое значение:
                        area(r) -> int
                        
        area(2) -> ~(4*3,1415)
        '''
        if r < 0:
                raise ValueError("Negative number")
        return math.pi * r * r


def perimeter(r):
        '''
        Функция perimeter(r) принимает один аргумент(радиус), возвращает длину окружности
                Параметры:
                        r(int)
                        
                Возвращаемое значение:
                        perimeter(r) -> int
                        
        perimeter(6) -> ~(12*3,1415)
        '''
        if r < 0:
                raise ValueError("Negative number")
        return 2 * math.pi * r


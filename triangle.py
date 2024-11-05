def area(a, h):
    '''
    Функция area принимает два аргумента, возвращает полупроизведение аргументов

        Параметры:
            a(int)
            h(int)
            
        Возвращаемое значение:
            area(a, h) -> float
            
    area(2,4) -> 4
    '''
    if a < 0 or h < 0:
        raise ValueError("Negative number")
    return a * (h / 2)

def perimeter(a, b, c):
    '''
    Функция perimeter принимает три аргумента, возвращает их сумму

        Параметры:
            a(int)
            b(int)
            c(int)
            
        Возвращаемое значение:
            perimeter(a, b, c) -> int

    perimeter(3, 4, 5) -> 12
    '''
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Negative number")
    return a + b + c

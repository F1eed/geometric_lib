def area(a):
    '''
    Функция area(a) принимает один аргумент, возвращает принятый аргумент в квадарте

        Параметры:
            a(int)
            
        Возвращаемое значение:
            area(a) -> int
    area(4) -> 16
    '''
    if a < 0:
        raise ValueError("Negative number")
    return a*a

def perimeter(a):
    '''
    Функция perimeter(a) принимает один аргумент возвращает принятый аргумент, умноженный в 4 раза

        Параметры:
            a(int)

        Возвращаемое значение:
            perimeter(a) -> int
            
    perimeter(2) -> 8
    '''
    if a < 0:
        raise ValueError("Negative number")
    return 4 * a

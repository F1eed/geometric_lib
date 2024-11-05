def area(a, b):
        '''
        Функция area(a, b) принимает два аргумента, возвращает их произведение
            Параметры:
                a(int)
                b(int)
                
            Возвращаемое значение:
                area(a, b) -> int
                
            area(5, 6) -> 30
        '''
        if a < 0 or b < 0:
                raise ValueError("Negative number")
        return a * b

def perimeter(a, b):
        '''
        Функция perimeter(a, b) принимает два аргумента, возвращает их удвоенную сумму
            Параметры:
                a(int)
                b(int)

            Возвращаемое значение:
                perimeter(a, b) -> int
                
            perimeter(5, 6) -> 22
        '''
        if a < 0 or b < 0:
                raise ValueError("Negative number")
        return 2*(a + b)

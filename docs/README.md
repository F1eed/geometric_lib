# DOCUMENTATION
  В данном репозитории хранятся файлы, вычисляющие площадь и периметр для четырех фигур: **квадрат, окружность, треугольник, прямоугольник**.
  ## Functions
  - ### triangle
  В файле [`triangle.py`](https://github.com/F1eed/geometric_lib/blob/main/triangle.py) содержится две функции: area и perimeter. Функция area принимает два аргумента, возвращает полупроизведение: `area(a, h) -> int, area(5,6) -> 15`. Функция perimeter принимает три аргумента, возвращает их сумму: `perimeter(a, b, c) -> int, perimeter(7, 8, 5) -> 20`
  - ### square
  В файле [`square.py`](https://github.com/F1eed/geometric_lib/blob/main/square.py) содержится две функции: area и perimeter. Функция area принимает аргумент, возвращает аргумент в квадрате: `area(a) -> int, area(5) -> 25`. Функция perimeter принимает аргумент, возвращает аргумент, умноженный на 4: `perimeter(a) -> int, perimeter(7) -> 28`
  - ### rectangle
  В файле [`rectangle.py`](https://github.com/F1eed/geometric_lib/blob/main/rectangle.py) содержится две функции: area и perimeter. Функция area принимает два аргумента, возвращает их произведение: `area(a, b) -> int, area(5, 4) -> 20`. Функция perimeter принимает два аргумента, возвращает произведение суммы аргументов: `perimeter(a, b) -> int, perimeter(7, 5) -> 24`
  - ### circle
  В файле [`circle.py`](https://github.com/F1eed/geometric_lib/blob/main/circle.py) содержится две функции: area и perimeter. Для работы функций нужно импортировать модуль `math`, чтобы мы могли обращаться к константной переменной `PI(math.pi)`, Функция area принимает аргумент, возвращает квадрат аргумента, умноженного на `PI`: `area(r) -> int, area(5) -> 25*~3.1415`. Функция perimeter принимает аргумент, возвращает удвоенный аргумент, умноженный на `PI`: `perimeter(r) -> int, perimeter(7) -> 14*~3.1415`
  ## Math formulas
  ### Area
  - Circle: S = πR²
  - Rectangle: S = ab
  - Square: S = a²

  ### Perimeter
  - Circle: P = 2πR
  - Rectangle: P = 2a + 2b
  - Square: P = 4a
# History
  ## Commit [7f740ffacd37f22fbbcb10754b92db276863b7ab](https://github.com/F1eed/geometric_lib/commit/7f740ffacd37f22fbbcb10754b92db276863b7ab)
  - ### обновил комментарии в файлах
  ## Commit [bb0e16cf86b268f2a9d9cfc03d660610bac43df9](https://github.com/F1eed/geometric_lib/commit/bb0e16cf86b268f2a9d9cfc03d660610bac43df9)
  - ### добавил файл rectangle.py и triangle.py, заменил ошибки
  ## Commit [d078c8d9ee6155f3cb0e577d28d337b791de28e2](https://github.com/F1eed/geometric_lib/commit/d078c8d9ee6155f3cb0e577d28d337b791de28e2)
  - ### L-03: Docs added
  ## Commit [8ba9aeb3cea847b63a91ac378a2a6db758682460](https://github.com/F1eed/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460)
  - ### L-03: Circle and square added

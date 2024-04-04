def say_triangle():
    print('ВОЗМОЖЕН ТРЕУГОЛЬНИК?')
    a = int(input('Введите длину первой стороны: '))
    b = int(input('Введите длину второй стороны: '))
    c = int(input('Введите длину третьей стороны: '))
    if a + b <= c or a + c <= b or b + c <= a or a == 0 or b == 0 or c == 0:
        print('треугольник невозможен')
    elif a == c and b == c:
        print('ЭТО РАВНОСТОРОННИЙ ТРЕУГОЛЬНИК!')
    elif a == c or b == c or a == b:
        print('ЭТО РАВНОБЕДРЕННЫЙ ТРЕУГОЛЬНИК!')
    else:
        print('ЭТО ТРЕУГОЛЬНИК!')



say_triangle()

import math
figure = input("Введите фигуру: ")
print('фигура', figure)
if(figure == 'круг'):
    r = int(input("Введите радиус: "))
    print('радиус', r)
    S = math.pi*r**2
    print(S)
elif(figure == 'треугольник'):
    A = int(input("Введите сторону А: "))
    B = int(input("Введите сторону В: "))
    C = int(input("Введите сторону С: "))
    print('стороны', A, B, C)
    p = (A+B+C)/2
    S = math.sqrt(p*(p-A)*(p-B)*(p-C))
    print(S)
elif(figure == 'прямоугольник'):
    A = int(input("Введите сторону А: "))
    B = int(input("Введите сторону В: "))
    S = A*B
    print(S)
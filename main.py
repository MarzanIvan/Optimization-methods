def almost_orthogonal_split(A):
    A = sorted(A)  # сортируем для жадного подхода
    n = len(A) // 2
    B = []
    C = []
    for i in range(n):
        if i % 2 == 0:
            B.append(A[i])
            C.append(A[-(i+1)])
        else:
            B.append(A[-(i+1)])
            C.append(A[i])
    return B, C

def scalar_product(B, C):
    return sum(b * c for b, c in zip(B, C))

# Пример:
A = [3, 7, -2, 4, 1, -5, 6, -8]  # длина 2n = 8
B, C = almost_orthogonal_split(A)
print("B:", B)
print("C:", C)
print("Скалярное произведение:", scalar_product(B, C))
print("Модуль:", abs(scalar_product(B, C)))

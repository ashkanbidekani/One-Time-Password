from random import uniform


def Gen():
    x = 0
    for _ in range(5):
        x = int(uniform(100000,1000000))
    return x


print(Gen())
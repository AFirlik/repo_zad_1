
pi = 3.14
def prostokat(a, b):
    pole = a*b
    obwod = 2*a + 2*b
    return pole, obwod

def kolo(r):
    pole = pi*(r**2)
    obwod = 2*pi*r
    return pole, obwod

print(f'Pole i obwod prostokata wynosza: {prostokat(10, 15)}')
print(f'Pole i obwod kola wynosza: {kolo(20)}')
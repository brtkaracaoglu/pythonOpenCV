#yield
"""
iteresyon -yineleme
geerator -yinelecileri değerlei bellekte saklamaz yeri gelince aninda üretirler
yield - fonksiyon eğer return olarak generetor döndürecekse bunu return yerine yield anahtarı gibi yapar
generator gibi döndürmesi dışında return gibi kullanılan bir anahtar sözcüktür.
"""
#yineleme
liste = [1,2,3]
for i in liste:
    print(i)

#generator
generator = (x for x in range(1,4))
for i in generator:
    print(i)

#yield
def createGenerator():
    liste = range(1,4)
    for i in liste:
        yield i

generator1 = createGenerator()
print(generator1)

for i in generator:
    print(i)
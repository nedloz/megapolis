file = open('space.txt').read().split('\n')
data = [el.split('*') for el in file]
# записываем координаты и направления в отдельные массивы
for el in data:
    el[2] = el[2].split()
    el[3] = el[3].split()
data.pop(0)
# print(data.pop(0), data)

for el in data:
    n = int(el[0].split('-')[1][0]) # первая цифра в номере корабля
    m = int(el[0].split('-')[1][1]) # вторая цифра в номере корабля
    t = len(el[1])  # кол-во букв в родной планете корабля
    # если x координата равна 0
    if el[2][0] == '0':
        if n > 5:
            # переопределяем x координату по формуле
            el[2][0] = str(n + int(el[3][0]))
        if n <= 5:
            # переопределяем x координату по формуле
            el[2][0] = str(-(n + int(el[3][0])) * 4 + t)
    if el[2][1] == '0': # если y координата равна 0
        if m > 3:
            # переопределяем y координату по формуле
            el[2][1] = str(m + t + int(el[3][1]))
        if m <= 3:
            # переопределяем y координату по формуле
            el[2][1] = str(-(n + int(el[3][1])) * m)

# возвращаем координатам и направлению прежний вид
for el in data:
    el[2] = el[2][0] + ' ' + el[2][1]
    el[3] = el[3][0] + ' ' + el[3][1]
# записываем все в новый файл
f = open('space_new.txt', 'w')
for el in data:
    f.write('*'.join(el)+'\n')
    if el[0].split('-')[0][-1] == 'V':
        print(el[0] + ' - (<' + el[2].split()[0]+'>, <' + el[2].split()[1] + '>)')

for el in data:
    el[2] = el[2].split()
    el[3] = el[3].split()

def getNum(name):
    code, num = name.split('-')
    return num

for i in range(1, len(data)):
    x = data[i]
    j = i
    while j > 0 and float(getNum(data[j-1][0])) > float(getNum(x[0])):
        data[j] = data[j-1]
        j-=1
    data[j]=x
b = data[:10]
for el in b:
    print(el[0])
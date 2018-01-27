a = int(input())
b = int(input())
for i in range(max(a, b)):
    a -= 1
    b -= 0.5
    if min(a, b) == 0:
        break
if a < b:
    print('Все такрелки вымыты. Осталось', b, 'ед. моющего средства')
elif a == b:
    print('Все тарелки вымыты, моющее средство закончилось')
else:
    print('Моющее средство закончилось. Осталось',int(a),'тарелок')

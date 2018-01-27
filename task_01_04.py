x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
a = (x - x1)**2 + (y - y1)**2
b = (x1 - x2)**2 + (y1 - y2)**2
c = (x - x2)**2 + (y - y2)**2
if bool((a + b)**2 == c**2) | bool((a + c)**2 == b**2) | bool((b + c)**2 == a**2):
    print('yes')
else:
    print('no')
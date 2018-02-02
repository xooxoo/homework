"""
def convert(expr):
    op = []
    num = []
    for i in expr:
        if i == '(' or i == ')':
            op.append(i)
        elif type(i) is int:
            num.append(i)
        elif i == '+' or i == '-':
            if '(' and ')' in op:
                op.remove('(')
                op.remove(')')
                num.append(op.pop())
            elif '+' or '-' in op:
                num.append(op.pop())
            else:
                op.append(i)
        elif i == '*' or '/':
            op.append(i)
        print(op, num)
print(convert([1, '+', '(', 3, '*', 4,')']))
"""

a = 'ghbdtn 2342345 ;khf'
b = list(''.join(a))
c = []
d = []
for i in b:
    if i.isdigit():
        c.append(i)
    else:
        d.append(i)
print(d,c)
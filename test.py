num = int(input('how many numbers would you like to add?'))
values = 0
L = []
while values < num:
    x = int(input('Next number'))
    L.append(x)
    values += 1

print(L)
op = input('do you want to add (a) or multiply (m)')

if op == 'm':
    total=1
    for n in L:
        total = total *n

elif op == 'a':
    total=0
    for n in L:
        total = total +n

print(total)
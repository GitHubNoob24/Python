num = int(input('how many numbers would you like to add?'))
value = 0
L = []

while value < num:
    numbers = int(input('type a number'))
    value += 1
    L.append(numbers)
    
print(L)

opp = input("Choose to multiply '*' or add '+': ")

if opp == '*':
    total = 1
    for n in L:
        total *= n
elif opp == '+':
    total = 0
    for n in L:
        total += n
else:
    total = "something went wrong"
     
print(total)



    



 


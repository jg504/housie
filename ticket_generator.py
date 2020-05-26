from random import randint

matrix = [[0 for i in range(9)] for j in range(3)]

def actual_gen():
    temp = [[0 for i in range(9)] for j in range(3)]

    for i in range(2):
        count = 0

        while count < 5:
            pos = randint(0, 8)
            
            if temp[i][pos] == 0:
                temp[i][pos] = 1
                count += 1

    count = 0
    for i in range(9):
        if temp[0][i] == temp[1][i] == 0:
            temp[2][i] = 1
            count += 1
    
    while count < 5:
        pos = randint(0, 8)
        
        if temp[2][pos] == 0:
            temp[2][pos] = 1
            count += 1

    return temp

def numbers(num, range):
    li = [0] * 3
    actual = [0] * num

    count = 0

    while num > count:
        temp = randint(1 + 10 * range, 9 + 10 * range)

        if temp != li[0] and temp != li[1] and temp != li[2]:
            li[count] = temp
            actual[count] = temp
            count += 1

    return actual

def pos_gen():
    temp = actual_gen()

    ticket = [[0 for i in range(9)] for j in range(3)]

    for i in range(9):
        count = 0

        for j in range(3):
            if temp[j][i] == 1:
                count += 1

        numb = numbers(count, i)

        numb.sort()

        count = 0
        for j in range(3):
            if temp[j][i] == 1:
                ticket[j][i] = numb[count]
                count += 1

    return ticket

ticket = pos_gen()

for i in range(3):
    for j in range(9):
        if ticket[i][j] != 0:
            print(ticket[i][j], end = "\t")
        
        else:
            print("X", end = "\t")
    print()
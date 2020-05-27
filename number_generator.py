from random import randint

def generator(li):
    num = randint(1, 90)

    if li[num - 1] == 1:
        num = generator(li)
    
    return num

def show(li):
    print()
    for i in range(90):
        if li[i] == 1:
            print(i + 1, end = " ")
        
        if i % 10 == 9:
            print()

li = [0] * 90

while True:
    choice = input("""
Press 1 for next number.
Press 2 to show board.
Press 0 to exit.

>>> """)
    
    if choice == "0":
        break

    elif choice == "1":
        new = generator(li)
        li[new - 1] = 1
        print("\n", new)
    
    elif choice == "2":
        show(li)
    
    else:
        print("Wrong choice. Try again.")
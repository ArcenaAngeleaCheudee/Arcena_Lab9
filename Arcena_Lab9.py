num = int(input("Enter the number of rows: "))

first_num = 1

for i in range(1, num + 1):
    for n in range(i):
        print(first_num, end=' ')
        first_num += 1 
    print()

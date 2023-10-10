
num_rows = 6 

current_num = 1

for i in range(1, num_rows + 1):
    for j in range(num_rows - i):
        print(" ", end=" ")
    
    for j in range(1, i + 1):
        print(current_num, end=" ")
        current_num += 1
    
    print()

#Design an algorithm that generates the first n numbers 
# in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

n = int(input("Enter the length of the sequence: ")) # Do not change this line
i1 = 1
i2 = 2
i3 = 3
sum_int = 0
count = 1
while count <= n:
    if count == 1:
        i1 = count
    elif count == 2:
        i2 = count
    elif count ==3:
        i3 = count
        i1 = i2 + i1
        i2 = i3 + i2
        i3 = sum_int
    else: 
        sum_int = i1 + i2 + i3
        i1 = i2
        i2 = i3
        i3 = sum_int
    count +=1
    print(sum_int)
i1 = i2 + i1
i2 = i3 + i2
i3 = sum_int


#Design an algorithm that generates the first n numbers 
# in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …
i1= -1+0+1 #= 0
i2 = i1+1+0 #= 1
i3 = i2+i1+1 #= 2
i4 = i3+i2+i1 #= 3
# 3+2+1=6
# 6+3+2=11
# 11+6+5=20

n = int(input("Enter the length of the sequence: ")) # Do not change this line

count = 1

while count <= n: 
    if count == 1:
        print(count)
        count +=1
    if count == 2:
        print(count)
        count +=1
    if count == 3:
        print(count)
        count +=1

print(i4)
    # i1 = i2
    # i2 = i3
    # i3 = sum_int

# i1 = i2 + i1
# i2 = i3 + i2
# i3 = sum_int

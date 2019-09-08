#Finds and prints all positive two digit numbers 
# whose square of the sum of its digits 
# is equal to the number.
for number in range(10, 100): 
#Find the first integer
    first_int = number//10 
#finds the secound integer
    secound_int = number%10 
#Sum of the two integers
    sum_int = first_int + secound_int 
#If number and the sum are equl, print number
    if number == sum_int**2:
        square = sum_int**2
        print(number,)

num = 0 
for pos_num in range(100,0, -1):
    count_div = 0
    for num in range(1, pos_num+1):
        if pos_num % num == 0:
            count_div += 1
            if count_div == 10:
                print(pos_num)
for number in range(10, 100): 
#Find the first integer
    first_int = number//10 
#finds the secound integer
    secound_int = number%10 
#Sum of the two integers
    sum_int = first_int + secound_int 
#If number and the sum are equl, print number
    if number == sum_int**2:
        print(number,"=", first_int, "+", secound_int, "=", sum_int)
        square = sum_int**2
        print(sum_int, "^2 =",square)
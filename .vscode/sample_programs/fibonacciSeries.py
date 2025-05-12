# Fibonacci Series if the number is is given as 8 , it needs to print the number as 0,1,1,2,3,5,8,13,21


def FibSeries(num):
    a, b = 0, 1
    print(a, end=" ")
    print(b, end=" ")
    for _ in range(2, num):
        c = a + b;
        a, b = b, c
        print(c, end=" ")  
    print()          
FibSeries(10)

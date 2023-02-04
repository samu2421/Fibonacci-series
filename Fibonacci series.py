#Fibonacci numbers

import math
 
def fibo(n):
    phi = (1 + math.sqrt(5)) / 2
    return round(pow(phi, n) / math.sqrt(5))
       
if __name__ == '__main__':
     
    n = int(input("Enter the no. of terms : "))
     
    print(fibo(n))
 

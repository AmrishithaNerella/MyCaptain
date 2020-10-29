def fibo_num(n):  
   if n <= 1:  
       return n  
   else:  
       return(fibo_num(n-1) + fibo_num(n-2))     
nterms = int(input("How many terms? "))  
if nterms <= 0:  
   print("Please enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(fibo_num(i))  

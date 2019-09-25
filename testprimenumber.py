def prime_test(n):
    
 if (n==1):
    return False
 
 elif (n==2):
    return True;
 
 else:
     for z in range(2,n):
        if(n % z==0):
          return False
     return True             
print(prime_test(10))



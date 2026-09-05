def is_prime(num):
    if num <= 1:
        return(False)
    else:
        prime = True

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                prime = False
                break
        else:
            return(prime)

n= int(input("Prime numbers till: "))
primes=[]
for i in range(1,n+1):
    if is_prime(i):
        primes.append(i)
if not primes:
    print("No primes")
else:   
    print(primes)

'''
When does the else block associated with a for loop
execute?

The else block associated with a for loop is executed when the for loop is completely exected.
the else block will not execute if the for loop is broken in between.

'''

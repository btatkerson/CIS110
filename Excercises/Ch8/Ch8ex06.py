import math
def isPrime(n):
    if n%2==0:
        return False
    factor=3
    while factor<=math.sqrt(n):
        if n% factor==0:
            return False
        factor=factor+2
    return True

def main():
    print("This program finds all the prime numbers up to N\n")
    n=int(input("Enter the upper limit, n:"))
    print("primes:1 2",end=' ')
    for i in range(2,n+1):
        if isPrime(i):
            print(i,end=' ')
    print("Done")
main()

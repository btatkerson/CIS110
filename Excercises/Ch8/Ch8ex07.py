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

def goldbach(x):
    cand=3
    while cand<x/2:
        other=x-cand
        if isPrime(cand) and isPrime(other):
            return cand
        cand=cand+2

def main():
    print("Goldbach checker\n")

    n=int(input("Enter an even natural number:"))
    if n%2!=0:
        print(n,"is not even!")
    else:
        prime1=goldbach(n)
        prime2=n-prime1
        print("{0}+{1}={2}".format(prime1,prime2,n))

main()

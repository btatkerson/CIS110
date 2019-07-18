def main():
    print("This program outputs a Syracuse sequence\n")
    n=int(input("Enter the initial value (an int>=1):"))
    while n!=1:
        print(int(n),end=' ')
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
    print(1)
main()

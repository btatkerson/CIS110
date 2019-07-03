def main():
    print("This program computes the average of three exam scores.")
    print()
    s1,s2,s3=eval(input("Enter three scores seperated by a comma: "))
    avg=(s1+s2+s3)/3
    print("The average of the score is: ",avg)
    input("Press <Enter> to quit.")
main()

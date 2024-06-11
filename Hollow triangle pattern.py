#hollow triangle 
n=int(input('Enter the number of rows: '))
e=input("Enter what you want to print : ")
for row in range(n):
    for col in range(n):
        if row==n-1 or col==0 or row==col:
            print( e ,end=' ')
        else:
            print(" ",end=' ')
    print("\n")

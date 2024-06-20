r=int(input("enter no of rows:"))
c=int(input("enter no of columns:"))
A=[]
for i in range(r):
    x=[]
    for j in range(c):
        (x.append(int(input("enter the element:"))))
    A.append(x)
    print("matrix is:")
for i in range(r):
        for j in range(c):
            print(A[i][j],end=" ")
        print()
'''import threading
import time
def  f_square(n):
    for i in n:
       time.sleep(0.5)
       print("square=",n*n)
def f_cube(m):
    for i in 5:
        time.sleep(0.3)
        print("cube= ",m*m*m)
a=[1,2,3,4]
t1=threading.Thread(target=f_square,args=(10))
t2=threading.Thread(target=f_cube,args=(101))
t1.start()
t2.start()
t1.join()
t2.join()'''
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(A[1])

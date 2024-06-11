def generate(n, arr, i):
    if i == n:
        print(*arr)
        return
    arr[i] = 0
    generate(n, arr, i + 1)
    arr[i] = 1
    generate(n, arr, i + 1)

# Example usage:
n=5
arr = [0] * n
generate(n, arr, 0)

#persistance storage
#permanent storage On the disk we can store in file or database/ permanent storage on the secondary storage device
#serialization or pickeling
#pickeling: conversion of python object to binary stream
#(list,tuple,dictionary)
#import pickle
#dump()
#load()
'''import pickle
obj=[1,"abc",2,25]
fp=open("csea.txt","wb")
pickle.dump(obj,fp)
fp=open("csea.txt","rb")
#unpickle=load(fp)
#print(unpickle)'''
#four modules
#pickle
#mashal
#shelve
#dbm

arr=[6,2,5,4,3]
print("before sort")
print(arr)
arr.sort()
print("ater sort")
print(arr)
def is_sorted(arr):
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            return True
        else:
            count=count+1
if(count>0):
           print("not in sorted")
else:
     print("is sorted")


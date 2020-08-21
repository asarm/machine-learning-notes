import numpy as np

arr = np.array([[2,5,7,9],[1,3,6,8]])
print(arr)
print()

print(np.sum(arr))
print(np.sum(arr[0]))
print(np.sum(arr[1]))
print(np.sum(arr,axis=0))
print(np.sum(arr,axis=1))

print()
#cumulative sum
print((np.cumsum(arr))) 
print((np.cumsum(arr,axis=1)))

print()
#concatenate
arr2 = np.array([[1,3,6,8],[2,5,7,9]])

arr3 = np.concatenate([arr,arr2],axis=1)
print(arr3)
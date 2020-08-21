import numpy as np

#creates an ranged array [x,y)
arr1 = np.arange(1,10,1)
print(len(arr1))

arr2 = np.arange(1.5,20,1.8)
print(arr2)
print()

#reshape
arr1 = np.reshape(arr1,(3,3))
print(f'{arr1}\n')

#transpose
transposed = np.transpose(arr1)
print(transposed)

print("\nFlatten:")
print(arr1.flatten())

print()
#we give number of elements in an array
arr = np.linspace(5, 100, num=4,dtype = np.int32)
print((arr))

arr = np.linspace(5, 11, num=4, endpoint=False) #11 dahil değil
print((arr))

arr = np.linspace(5, 11, num=4, dtype=np.int32)  #uç değer (11) dahil
print((arr))

#zeros and ones
arr = np.zeros(4)
print(repr(arr))

arr = np.ones((2, 3))
print(repr(arr))

arr = np.ones((2, 3), dtype=np.int32)
print(repr(arr))

arr = np.array([[1, 2], [3, 4]])
print(repr(np.zeros_like(arr)))

arr = np.array([[0., 1.], [1.2, 4.]])
print(repr(np.ones_like(arr)))
print(repr(np.ones_like(arr, dtype=np.int32)))

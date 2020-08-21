import numpy as np

arr = np.array([[0, 2, 3],
                [-1, 3, -6],
                [-3, -2, 1]])

print((arr<=1))
print()
print(~(arr<=1))

arr2 = np.array([[0, 2, 3],
                [1, 3, -6],
                [-3, -2, np.nan]])
print()
print(np.isnan(arr2))

arr3 = np.array([2,3,5,72,2])
print((np.where(arr3 == 2)))

arr4 = np.array([10,4,7,9,2])
print(np.where(arr3>3,arr4,np.nan)) # F F T T F, 10 4 7 9 2, replace F with 0

x,y = np.where(arr >1)
print(arr[x,y])

print(repr(np.any(arr > 0, axis=0))) #col
print(repr(np.any(arr > 0, axis=1))) #row
print(repr(np.all(arr > 0, axis=1))) #row
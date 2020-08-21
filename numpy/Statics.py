import numpy as np

arr = np.array([[0, 72, 3],
                [1, 3, -60],
                [-3, -2, 4]])

print(arr.min())
print(np.max(arr))
print(np.argmax(arr)) #returns index
print()

print(np.mean(arr))
print(np.var(arr)) #varyans
print(np.var(arr,axis=0))
print(np.median(arr))
print(repr(np.median(arr, axis=0)))


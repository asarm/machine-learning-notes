import numpy as np

np.random.seed(1)
print(np.random.randint(1,20,size=10)) 

np.random.seed(2)
print(np.random.randint(1,20,size=10)) 

np.random.seed(1)
print(np.random.randint(1,20,size=10)) 


#shuffle an array
arr = np.array([1,2,3,4])
print(arr)
np.random.shuffle(arr)
print(arr)


#random.uniform
print(np.random.uniform(low=-1.5, high=2.2))

#random.normal
print(np.random.normal())
print(np.random.normal(loc=1.5, scale=3.5))
print(repr(np.random.normal(loc=-2.4, scale=4.0,
                            size=(2, 2))))

#choice from array
colors = ['red', 'blue', 'green']
print(np.random.choice(colors))
#choice multiple
print(np.random.choice(colors, size=2))
#with probability
print(np.random.choice(colors,p=[0.6, 0.2, 0.2]))
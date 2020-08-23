import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'satıs':[20,28,30,22],'alıs':[10,25,33,14]})

df.plot(title='Alıs-Satıs')
plt.xlabel('Gün')
plt.ylabel('Miktar')

df.plot(kind='hist')
df.plot(kind='box')
plt.show()
plt.savefig('df.png')
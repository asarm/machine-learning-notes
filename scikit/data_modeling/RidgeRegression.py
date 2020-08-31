import numpy as np
from sklearn import linear_model

pizza_data = np.array([[2100,800],[2500,850],[1800,760],[2000,800],[2300,810]]) #Calorie - weight 
pizza_prices = np.array([10.99, 12.5 ,  9.99, 10.99, 11.99])


alphas = [0.1, 0.2, 0.3]
reg = linear_model.RidgeCV(alphas = alphas)
#reg = linear_model.Ridge(alpha=0.1)
reg.fit(pizza_data,pizza_prices)
print(f"Coefficients:{reg.coef_}")
print('Intercept: {}\n'.format(reg.intercept_))
    
r2 = reg.score(pizza_data, pizza_prices)
print('R2: {}\n'.format(r2))
print('Chosen alpha: {}\n'.format(reg.alpha_))
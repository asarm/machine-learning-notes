import numpy as np
from sklearn import linear_model

pizza_data = np.array([[2100,800],[2500,850],[1800,760],[2000,800],[2300,810]]) #Calorie - weight 
pizza_prices = np.array([10.99, 12.5 ,  9.99, 10.99, 11.99])

reg = linear_model.LinearRegression()
reg.fit(pizza_data,pizza_prices) #model is ready

new_pizzas = np.array([[2000,  820],
                       [2200,  830]])

price_predicts = reg.predict(new_pizzas)
print(price_predicts)


print('Coefficients: {}\n'.format(repr(reg.coef_)))
print('Intercept: {}\n'.format(reg.intercept_))


#How fit linear regression model is to this data (0-1)
r2 = reg.score(pizza_data,pizza_prices)
print(f'Score is {r2}')
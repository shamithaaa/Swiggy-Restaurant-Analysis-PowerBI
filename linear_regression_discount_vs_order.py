import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

data = {
    'Restaurant': ['Noodle West', 'The Street Food Hub', 'Desi Tadka', 'Punjabi Tadka', 'Biryani Bliss'],
    'Discount (X)': [450, 490, 390, 380, 280],
    'Ava_Order_value (Y)': [5000, 7000, 3000, 7000, 6000]
}

df = pd.DataFrame(data)

x = df['Discount (X)'].values.reshape(-1, 1)
y = df['Ava_Order_value (Y)']

model = LinearRegression()
model.fit(x, y)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', label='Data points')

plt.plot(x, model.predict(x), color='red', label='Regression line')

plt.xlabel('Discount (X)')
plt.ylabel('Average Order Value (Y)')
plt.title('Discount vs. Average Order Value')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
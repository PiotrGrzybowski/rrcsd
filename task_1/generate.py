import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set seed for reproducibility
np.random.seed(0)

# Generate sample data
n = 1000
date_range = [(datetime.today() - timedelta(days=i)).date() for i in range(n)]
products = ['Product_A', 'Product_B', 'Product_C', 'Product_D']
prices = np.random.uniform(10, 100, size=n).round(2)
quantities = np.random.randint(1, 10, size=n)
payment_types = ['Cash', 'Credit Card', 'Debit Card', 'Online']

data = {
    'Date': random.choices(date_range, k=n),
    'Product': random.choices(products, k=n),
    'Price': prices,
    'Quantity': quantities,
    'Payment_Type': random.choices(payment_types, k=n)
}

df = pd.DataFrame(data)
print(df)
df.to_csv('sales_data.csv', index=False)



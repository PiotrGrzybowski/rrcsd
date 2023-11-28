"""
Tasks:
- Inspection:
  - Load the dataset into a Pandas DataFrame.
  - Display the first 5 rows of the DataFrame.
  - Convert the Date column to a DateTime type.

- Analysis:
  - Find unique Products names
  - Calculate and display the total sales revenue (Price * Quantity) for the dataset.
  - Add new column named code that contains the last 3 characters of the Product name.
  - Find the average price of products sold.
  - Group the data by Product and calculate the total quantity sold for each product.
"""

from pathlib import Path
import pandas as pd


def main():
    file_name = Path('sales_data.csv')
    df = pd.read_csv(file_name)
    print(df)


if __name__ == "__main__":
    main()


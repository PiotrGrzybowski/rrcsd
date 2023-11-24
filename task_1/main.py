from pathlib import Path
import pandas as pd

def load_and_inspect_data(path: Path) -> pd.DataFrame:
    pass

def format_data(df: pd.DataFrame) -> pd.DataFrame:
    pass

def calculate_total_sales(df: pd.DataFrame):
    pass

def calculate_average_price(df: pd.DataFrame):
    pass

def find_highest_sales_product(df: pd.DataFrame):
    pass

def total_quantity_per_product(df: pd.DataFrame):
    pass

def most_popular_payment_type(df: pd.DataFrame):
    pass

def main():
    file_name = Path('sales_data.csv')
    df = load_and_inspect_data(file_name)

    total_revenue = calculate_total_sales(df)
    average_price = calculate_average_price(df)
    highest_sales_product = find_highest_sales_product(df)
    quantity_per_product = total_quantity_per_product(df)
    popular_payment_type = most_popular_payment_type(df)

    print(f"Total Sales Revenue: {total_revenue}")
    print(f"Average Price of Products: {average_price}")
    print(f"Product with the Highest Sales Quantity: {highest_sales_product}")
    print(f"Total Quantity Sold per Product:\n{quantity_per_product}")
    print(f"Most Popular Payment Type: {popular_payment_type}")

if __name__ == "__main__":
    main()


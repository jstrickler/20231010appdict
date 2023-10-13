import pandas as pd

columns = "region country item_type sales_channel priority order_date order_id ship_date sold price cost".split()
df = pd.read_csv('../DATA/sales_records.csv', dtype={'Order ID': str}, names=columns)  # Read CSV data into dataframe. Pandas automatically uses the first row as column names

print(df.describe())  # Get statistics on the numeric columns (use `df.describe(include='O')` for text columns)
print()

print(df.info())  # Get information on all the columns ('object' means text/string)
print()

print(df.head(5))  # Display first 5 rows of the dataframe (`df.describe(__n__)` displays n rows)

# df['total_sales'] = df['sold'] * df['cost']  # add a total sales column
print(df)

print(df.info())
print(df.describe())
print(df.head(5))

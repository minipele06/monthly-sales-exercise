#monthly-sales-exercise

import os

import pandas

def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71

csv_filepath = os.path.join((os.path.dirname(__file__)), "..", "data", "monthly_sales.csv")

sales = pandas.read_csv(csv_filepath)

product_totals = sales.groupby(["product"]).sum()

product_totals = product_totals.sort_values("sales price", ascending=False)

total_sales = sales["sales price"].sum()

print("SALES REPORT (NOVEMBER 2018)")
print("")
print(f"TOTAL SALES: {to_usd(total_sales)}")
print("")
print("TOP SELLING PRODUCTS")
for x in range(0,3):
    print(f"{x+1}. {product_totals.index[x]}: {to_usd(product_totals['sales price'][x])}")


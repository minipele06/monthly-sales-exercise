#monthly-sales-exercise

import os

import pandas

csv_filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "data", "monthly_sales.csv")

df = pandas.read_csv(csv_filepath)

best_seller = df.groupby(["product"]).sum()

best_seller = best_seller.sort_values(by=["sales price"], ascending=False)

sales = df.to_dict("records")

#best_seller = best_seller.to_dict("records")

#best_seller_sorted = sorted(best_seller, key=lambda x: x["sales price"])

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444
    
    Example: to_usd(4000.444444)
    
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

total_sales = 0

for x in sales:
    total_sales += x["sales price"]

print("SALES REPORT (NOVEMBER 2018)")
print("")
print(f"TOTAL SALES: {to_usd(total_sales)}")
print("")
print("TOP SELLING PRODUCTS")
print(best_seller.columns[0])
print(f"1. {to_usd(best_seller['sales price'][0])}")


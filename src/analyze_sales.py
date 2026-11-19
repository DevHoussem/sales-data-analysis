import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
#prepare input and output files
base_dir=Path(__file__).resolve().parent.parent
input_file=base_dir/"data"/"processed"/"superStore_clean.csv"
output_dir=base_dir/"reports"
output_dir.mkdir(parents=True,exist_ok=True)
#prepare some datas before analyse them
df = pd.read_csv(input_file)
df["order_date"] = pd.to_datetime(df["order_date"])
print("dataset loaded successfully")
print("\ntotal records:",len(df))
#general business KPIs
total_sales = df["sales"].sum()
total_profit = df["profit"].sum()
total_orders = df["order_id"].nunique()
total_customers = df["customer_name"].nunique()
total_quantity = df["quantity"].sum()
if total_sales != 0:
    kpi_calculation=(total_profit/total_sales)*100 
else:
    kpi_calculation=0
print("\nBusiness KPIs")
print(f"total sales: {total_sales:,.2f}")
print(f"total profit: {total_profit:,.2f}")
print(f"total orders: {total_orders}")
print(f"total customers: {total_customers}")
print(f"total quantity Sold: {total_quantity:,.0f}")
print(f"profit margin: {kpi_calculation:.2f}%")
#SALES BY CATEGORY
sales_by_category = (df.groupby("category")["sales"].sum().sort_values(ascending=False))
print("\nSales by category")
print(sales_by_category)
#PROFIT BY CATEGORY
profit_by_category = (df.groupby("category")["profit"].sum().sort_values(ascending=False))
print("\nprofit by category")
print(profit_by_category)
# SALES BY REGION
sales_by_region = (df.groupby("region")["sales"].sum().sort_values(ascending=False))
print("\nsales by region")
print(sales_by_region)
# PROFIT BY REGION
profit_by_region= (df.groupby("region")["profit"].sum().sort_values(ascending=False))
print("\nprofit by region")
print(profit_by_region)
#TOP 10 SUB-CATEGORIES
top_products = (df.groupby("sub_category")["sales"].sum().sort_values(ascending=False).head(10))
print("\nTop 10 sub-categories")
print(top_products)
# MONTHLY SALES
df["year_month"] = df["order_date"].dt.to_period("M").astype(str)
monthly_sales = (df.groupby("year_month")["sales"].sum().sort_index())
print("\nmonthly sales")
print(monthly_sales)

# VISUALIZATIONS
sns.set_theme(style="whitegrid")
# Chart 1: Sales by category
plt.figure(figsize=(9, 5))
sns.barplot(
    x=sales_by_category.index,
    y=sales_by_category.values
)
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig(output_dir / "sales_by_category.png")
plt.show()

# Chart 2: Profit by region
profit_by_region = df.groupby("region")["profit"].sum().sort_values(
    ascending=False
)

plt.figure(figsize=(9, 5))
sns.barplot(
    x=profit_by_region.index,
    y=profit_by_region.values
)
plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig(output_dir / "profit_by_region.png")
plt.show()


# Chart 3: Monthly sales trend
plt.figure(figsize=(12, 5))
plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(output_dir / "monthly_sales.png")
plt.show()


# Chart 4: Top 10 sub-categories
plt.figure(figsize=(10, 6))
sns.barplot(
    x=top_products.values,
    y=top_products.index
)
plt.title("Top 10 Sub-Categories by Sales")
plt.xlabel("Sales")
plt.ylabel("Sub-Category")
plt.tight_layout()
plt.savefig(output_dir / "top_10_subcategories.png")
plt.show()

# EXPORT ANALYSIS RESULTS
sales_by_category.to_csv(output_dir / "sales_by_category.csv")
profit_by_category.to_csv(output_dir / "profit_by_category.csv")
sales_by_region.to_csv(output_dir / "sales_by_region.csv")
top_products.to_csv(output_dir / "top_10_subcategories.csv")
monthly_sales.to_csv(output_dir / "monthly_sales.csv")
print("\nAnalysis completed successfully!")
print("Charts and analysis files saved in the reports folder.")

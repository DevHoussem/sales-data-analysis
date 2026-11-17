import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

base_dir=Path(__file__).resolve().parent.parent

input_file=base_dir/"data"/"processed"/"superStore_clean.csv"
output_dir=base_dir/"reports"
output_dir.mkdir(parents=True,exist_ok=True)
df = pd.read_csv(input_file)
df["order_date"] = pd.to_datetime(df["order_date"])

print("dataset loaded successfully")
print("total records:",len(df))

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
print("\n========== BUSINESS KPIs ==========")
print(f"Total Sales: {total_sales:,.2f}")
print(f"Total Profit: {total_profit:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Total Customers: {total_customers}")
print(f"Total Quantity Sold: {total_quantity:,.0f}")
print(f"Profit Margin: {kpi_calculation:.2f}%")

# 3. SALES BY CATEGORY

sales_by_category = (df.groupby("category")["sales"].sum().sort_values(ascending=False))

print("\n========== SALES BY CATEGORY ==========")
print(sales_by_category)

# 4. PROFIT BY CATEGORY
profit_by_category = (df.groupby("category")["profit"].sum().sort_values(ascending=False))
print("\n========== PROFIT BY CATEGORY ==========")
print(profit_by_category)

# 5. SALES BY REGION
sales_by_region = (df.groupby("region")["sales"].sum().sort_values(ascending=False))

print("\n========== SALES BY REGION ==========")
print(sales_by_region)


# 6. TOP 10 SUB-CATEGORIES

top_products = (
    df.groupby("sub_category")["sales"].sum().sort_values(ascending=False).head(10))

print("\n========== TOP 10 SUB-CATEGORIES ==========")
print(top_products)

# 7. MONTHLY SALES
df["year_month"] = df["order_date"].dt.to_period("M").astype(str)
monthly_sales = (df.groupby("year_month")["sales"].sum().sort_index())

print("\n========== MONTHLY SALES ==========")
print(monthly_sales)

# 8. DISCOUNT AND PROFIT ANALYSIS
discount_analysis = (df.groupby("discount").agg(total_sales=("sales", "sum"),total_profit=("profit", "sum"),average_profit=("profit", "mean"),order_count=("order_id", "nunique")).sort_index())
print("\n========== DISCOUNT ANALYSIS ==========")
print(discount_analysis)

# 9. VISUALIZATIONS
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


# ==============================
# 10. EXPORT ANALYSIS RESULTS
# ==============================

sales_by_category.to_csv(output_dir / "sales_by_category.csv")
profit_by_category.to_csv(output_dir / "profit_by_category.csv")
sales_by_region.to_csv(output_dir / "sales_by_region.csv")
top_products.to_csv(output_dir / "top_10_subcategories.csv")
monthly_sales.to_csv(output_dir / "monthly_sales.csv")
discount_analysis.to_csv(output_dir / "discount_analysis.csv")

print("\nAnalysis completed successfully!")
print("Charts and analysis files saved in the reports folder.")

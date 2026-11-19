import os
import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine, URL, text

# Project paths
base_dir = Path(__file__).resolve().parent.parent
csv_file = base_dir / "data" / "processed" / "superStore_clean.csv"
# Database connection
connection_url = URL.create(
    "mysql+pymysql",
    username="root",
    password="",
    host="localhost",
    port=3306,
    database="sales_analytics"
)
engine = create_engine(connection_url)

try:
    # Read cleaned CSV
    df = pd.read_csv(csv_file)
    # Prepare date column
    df["order_date"] = pd.to_datetime( df["order_date"],errors="coerce").dt.date
    # Select the database column
    columns = [
        "order_id",
        "order_date",
        "customer_name",
        "region",
        "category",
        "sub_category",
        "sales",
        "quantity",
        "discount",
        "profit"
    ]
    df = df[columns]
    # Replace existing imported records, then insert fresh data
    with engine.begin() as connection:
        connection.execute(text("DELETE FROM sales"))
        df.to_sql(
            name="sales",
            conn=connection,
            if_exists="append",
            index=False,
        )
    print("Data imported successfully!")
    print("Rows imported:", len(df))
except Exception as error:
    print("An error occurred:", error)
finally:
    engine.dispose()

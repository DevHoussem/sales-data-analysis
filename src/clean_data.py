import pandas as pd
from pathlib import Path
#prepare input and output files
base_dir=Path(__file__).resolve().parent.parent
input_file=base_dir/"data"/"raw"/"SuperStoreOrders.csv"
output_file=base_dir/"data"/"processed"/"superStore_clean.csv"
#show the original dataset
df=pd.read_csv(input_file)
print("original dataset: ")
print("rows:",len(df))
print("columns:",len(df.columns))
# clean columns names
df.columns=df.columns.str.strip().str.lower().str.replace(" ","_")
# remove duplicates
duplicates= df.duplicated().sum()
df= df.drop_duplicates()
# convert order dates from str to datetime
df["order_date"]=pd.to_datetime(df["order_date"],dayfirst=True,errors="coerce")
#convert numeric coluumns
numeric_columns=["sales","quantity","discount","profit"]
for column in numeric_columns:
    df[column]=pd.to_numeric(df[column],errors="coerce")
# remove rows missing essential information
df=df.dropna(subset=["order_id","order_date","sales"])
#fill missing values by null
categorical_columns=["customer_name","region","category","sub_category"]
for column in categorical_columns:
    df[column]=df[column].fillna("NULL")
# Fill missing quantity and discount with their medians
for column in ["quantity", "discount"]:
    df[column] = df[column].fillna(df[column].median())
#remove unnecessary spaces from text
for column in categorical_columns:
    df[column] = df[column].str.strip()
#show the result dataset
print("\ncleaned dataset ")
print("Rows:", len(df))
print("Columns:", len(df.columns))
#show the missing values of the result dataset
print("\nMissing values after cleaning:")
print(df.isnull().sum())
#show the duplicated rows of the result dataset
print("\nDuplicate rows after cleaning:")
print(df.duplicated().sum())
#show its info
print(df.info())

# Save cleaned dataset into output csv file
output_file.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_file, index=False)

print("\nCleaned dataset saved successfully!")
print("File:", output_file)

import pandas as pd

df=pd.read_csv("data/raw/SuperStoreOrders.csv")
print(df.head())

# dataset infos
print("\n dataset info")
print(df.info())
# display dimensions
print("rows:",df.shape[0])
print("columns:",df.shape[1])
#statistical summary 
print("\n statistical summary")
print(df.describe())
#missing values
print("\n missing values")
print(df.isnull().sum())
#duplicated rows
print("\n duplicated rows")
print(df.duplicated().sum())
#Unique values in categorical columns
print("\n category ")
print(df["category"].unique())
print("\n region")
print(df["region"].unique())
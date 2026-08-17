#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
print(os.getcwd())


# In[9]:


import os

path = r"C:\Users\prajw\OneDrive\Documents\Zomato_project\Data.csv"

print("File exists:", os.path.exists(path))
print("File path:", path)


# In[10]:


import os

folder = r"C:\Users\prajw\OneDrive\Documents\Zomato_project"

print(os.listdir(folder))


# In[11]:


import os

path = r"C:\Users\prajw\OneDrive\Documents\Zomato_project\Data.csv"

print(os.path.exists(path))


# In[12]:


folder = r"C:\Users\prajw\OneDrive\Documents\Zomato_project"

print(os.listdir(folder))


# In[13]:


import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\prajw\OneDrive\Documents\Zomato_project\Data.csv.csv")

print("Dataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())


# In[15]:


df.duplicated().sum()


# In[16]:


df.nunique().sort_values()


# In[17]:


df["rate"].value_counts(dropna=False).head(20)


# In[18]:


df["approx_cost(for two people)"].value_counts(dropna=False).head(20)


# In[20]:


restaurant_counts = df["name"].value_counts()
print(restaurant_counts.head(20))


# In[21]:


print("Restaurants appearing more than once:",
      (restaurant_counts > 1).sum())


# In[22]:


print("Maximum appearances of one restaurant:",
      restaurant_counts.max())


# In[23]:


print("Maximum appearances of one restaurant:",
      restaurant_counts.min())


# In[24]:


print(df["rate"].unique())


# In[25]:


print(df["rate"].value_counts(dropna=False).tail(20))


# In[26]:


print(df["approx_cost(for two people)"].unique())


# In[27]:


print(df["approx_cost(for two people)"].tail(20))


# In[28]:


print(df["online_order"].value_counts(dropna=False))


# In[29]:


print(df["book_table"].value_counts(dropna=False))


# In[30]:


print(df["listed_in(type)"].value_counts().head(10))


# In[31]:


ccd = df[df["name"] == "Cafe Coffee Day"]

print(ccd.shape)


# In[32]:


print(
    ccd[
        [
            "name",
            "location",
            "rest_type",
            "rate",
            "votes",
            "cuisines",
            "approx_cost(for two people)",
            "listed_in(type)",
            "listed_in(city)"
        ]
    ].head(20)
)


# In[33]:


print("Unique locations:",
      ccd["location"].nunique())


# In[34]:


print(ccd["location"].value_counts())


# In[35]:


print(
    ccd[
        ["location", "listed_in(type)", "listed_in(city)"]
    ].drop_duplicates().head(30)
)


# In[36]:


print(
    df.duplicated(
        subset=["name", "location"]
    ).sum()
)


# In[37]:


ccd_sarjapur = df[
    (df["name"] == "Cafe Coffee Day") &
    (df["location"] == "Sarjapur Road")
]

print(ccd_sarjapur.shape)


# In[38]:


print(
    ccd_sarjapur[
        [
            "name",
            "location",
            "rate",
            "votes",
            "online_order",
            "book_table",
            "approx_cost(for two people)",
            "listed_in(type)",
            "listed_in(city)"
        ]
    ]
)


# In[39]:


print(
    ccd_sarjapur[
        [
            "name",
            "location",
            "rate",
            "votes",
            "online_order",
            "book_table",
            "rest_type",
            "cuisines",
            "approx_cost(for two people)"
        ]
    ].drop_duplicates()
)


# In[40]:


ccd_sarjapur = df[
    (df["name"] == "Cafe Coffee Day") &
    (df["location"] == "Sarjapur Road")
]

print(ccd_sarjapur.shape)


# In[41]:


print(
    ccd_sarjapur[
        [
            "name",
            "location",
            "rate",
            "votes",
            "online_order",
            "book_table",
            "rest_type",
            "cuisines",
            "approx_cost(for two people)",
            "listed_in(type)",
            "listed_in(city)"
        ]
    ]
)


# In[42]:


print(
    df.duplicated(
        subset=[
            "name",
            "location",
            "rate",
            "votes",
            "online_order",
            "book_table",
            "rest_type",
            "cuisines",
            "approx_cost(for two people)"
        ]
    ).sum()
)


# In[43]:


core_cols = [
    "name",
    "location",
    "rate",
    "votes",
    "online_order",
    "book_table",
    "rest_type",
    "cuisines",
    "approx_cost(for two people)"
]

core_unique = df.drop_duplicates(subset=core_cols)

print("Original rows:", len(df))
print("After core deduplication:", len(core_unique))
print("Rows removed:", len(df) - len(core_unique))


# In[44]:


print(core_unique.head())


# In[45]:


print(core_unique.shape)


# In[46]:


print(core_unique["name"].nunique())


# In[47]:


print(core_unique["location"].nunique())


# In[48]:


print(
    core_unique.duplicated(
        subset=["name", "location"]
    ).sum()
)


# In[50]:


clean_df = df.copy()


# In[51]:


print(clean_df.shape)


# In[52]:


clean_df = clean_df.rename(columns={
    "approx_cost(for two people)": "approx_cost",
    "listed_in(type)": "listed_type",
    "listed_in(city)": "listed_city",
    "rest_type": "restaurant_type"
})


# In[53]:


print(clean_df.columns.tolist())


# In[54]:


clean_df = df.copy()

clean_df = clean_df.rename(columns={
    "approx_cost(for two people)": "approx_cost",
    "listed_in(type)": "listed_type",
    "listed_in(city)": "listed_city",
    "rest_type": "restaurant_type"
})

print(clean_df.shape)
print(clean_df.columns.tolist())


# In[55]:


print(clean_df["rate"].value_counts(dropna=False).head(20))


# In[58]:


clean_df["rate"] = (
    clean_df["rate"]
    .astype(str)
    .str.replace("/5", "", regex=False)
    .str.strip()
    .replace(["NEW", "-"], np.nan)
)


# In[59]:


clean_df["rate"] = pd.to_numeric(
    clean_df["rate"],
    errors="coerce"
)


# In[60]:


print(clean_df["rate"].dtype)


# In[61]:


print(clean_df["rate"].describe())


# In[62]:


print(clean_df["rate"].isnull().sum())


# In[63]:


clean_df["rate"] = (
    clean_df["rate"]
    .astype(str)
    .str.replace("/5", "", regex=False)
    .str.strip()
    .replace(["NEW", "-"], np.nan)
)

clean_df["rate"] = pd.to_numeric(
    clean_df["rate"],
    errors="coerce"
)

print("Data type:", clean_df["rate"].dtype)

print("\nRating statistics:")
print(clean_df["rate"].describe())

print("\nMissing ratings:")
print(clean_df["rate"].isnull().sum())


# In[64]:


print(clean_df["rate"].isnull().sum())
print(clean_df["rate"].isnull().mean() * 100)


# In[65]:


clean_df[clean_df["rate"].isnull()][
    ["name", "rate", "votes", "restaurant_type"]
].head(10)


# In[66]:


rated_df = clean_df[clean_df["rate"].notna()].copy()

print(rated_df.shape)


# In[67]:


rated_df["rate"].describe()


# In[68]:


clean_df


# In[69]:


clean_df = clean_df.dropna(subset=["rate"])


# In[70]:


print(
    pd.crosstab(
        clean_df["rate"].isna(),
        clean_df["votes"] == 0,
        normalize="index"
    ) * 100
)


# In[71]:


print("Missing ratings:", clean_df["rate"].isna().sum())

print("Zero votes:", (clean_df["votes"] == 0).sum())

print(
    clean_df.loc[
        clean_df["rate"].isna(),
        "votes"
    ].value_counts().head(10)
)


# In[72]:


print(clean_df["rate"].dtype)
print(clean_df["votes"].dtype)


# In[73]:


print("Total rows:", len(clean_df))

print("Missing ratings:", clean_df["rate"].isna().sum())

print("Zero votes:", (clean_df["votes"] == 0).sum())

print("\nVotes among missing-rating restaurants:")
print(
    clean_df.loc[
        clean_df["rate"].isna(),
        "votes"
    ].value_counts().head(10)
)


# In[74]:


print(clean_df["votes"].dtype)

print(clean_df["votes"].describe())

print("\nMissing votes:")
print(clean_df["votes"].isna().sum())


# In[75]:


missing_rate = clean_df["rate"].isna()

print("Restaurants with missing rating:", missing_rate.sum())

print(
    "Missing rating + zero votes:",
    ((clean_df["rate"].isna()) & (clean_df["votes"] == 0)).sum()
)

print(
    "Missing rating + votes > 0:",
    ((clean_df["rate"].isna()) & (clean_df["votes"] > 0)).sum()
)


# In[76]:


print(clean_df.isnull().sum())


# In[77]:


print(clean_df.shape)
print(clean_df.dtypes)


# In[78]:


clean_df["restaurant_type"] = clean_df["restaurant_type"].fillna("Unknown")

clean_df["dish_liked"] = clean_df["dish_liked"].fillna("Not Available")

clean_df["cuisines"] = clean_df["cuisines"].fillna("Unknown")


# In[79]:


clean_df = clean_df.copy()


# In[81]:


clean_df["restaurant_type"] = clean_df["restaurant_type"].fillna("Unknown")

clean_df["dish_liked"] = clean_df["dish_liked"].fillna("Not Available")

clean_df["cuisines"] = clean_df["cuisines"].fillna("Unknown")


# In[82]:


print(clean_df[["restaurant_type", "dish_liked", "cuisines"]].isnull().sum())


# In[83]:


print(clean_df.isnull().sum())


# In[84]:


print(clean_df["approx_cost"].head(20))

print("\nUnique values:")
print(clean_df["approx_cost"].unique()[:30])


# In[85]:


print(clean_df["approx_cost"].head(20))

print("\nUnique values:")
print(clean_df["approx_cost"].unique()[:30])


# In[86]:


print("Number of unique cost values:", clean_df["approx_cost"].nunique())


# In[88]:


# Make sure clean_df is an independent DataFrame
clean_df = clean_df.copy()

# -----------------------------
# 1. Handle missing categorical values
# -----------------------------
clean_df["restaurant_type"] = clean_df["restaurant_type"].fillna("Unknown")
clean_df["dish_liked"] = clean_df["dish_liked"].fillna("Not Available")
clean_df["cuisines"] = clean_df["cuisines"].fillna("Unknown")

# -----------------------------
# 2. Clean approx_cost
# -----------------------------
clean_df["approx_cost"] = (
    clean_df["approx_cost"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.strip()
    .replace(["nan", "None", ""], np.nan)
)

clean_df["approx_cost"] = pd.to_numeric(
    clean_df["approx_cost"],
    errors="coerce"
)

# -----------------------------
# 3. Final missing-value check
# -----------------------------
print("Missing values:")
print(clean_df.isnull().sum())

# -----------------------------
# 4. Final data types
# -----------------------------
print("\nData types:")
print(clean_df.dtypes)

# -----------------------------
# 5. Dataset shape
# -----------------------------
print("\nDataset shape:", clean_df.shape)


# In[90]:


print("Duplicate rows:", clean_df.duplicated().sum())

print("\nRate range:")
print("Minimum:", clean_df["rate"].min())
print("Maximum:", clean_df["rate"].max())

print("\nVotes:")
print("Minimum:", clean_df["votes"].min())
print("Maximum:", clean_df["votes"].max())

print("\nApproximate cost:")
print("Minimum:", clean_df["approx_cost"].min())
print("Maximum:", clean_df["approx_cost"].max())


# In[91]:


print("Invalid ratings:", ((clean_df["rate"] < 0) | (clean_df["rate"] > 5)).sum())

print("Negative votes:", (clean_df["votes"] < 0).sum())

print("Negative costs:", (clean_df["approx_cost"] < 0).sum())


# In[92]:


# ============================================
# EDA PART 1 — DATASET OVERVIEW
# ============================================

print("Dataset Shape:", clean_df.shape)

print("\nNumber of Restaurants:", clean_df["name"].nunique())

print("\nNumber of Locations:", clean_df["location"].nunique())

print("\nNumber of Restaurant Types:", clean_df["restaurant_type"].nunique())

print("\nNumber of Cuisines:", clean_df["cuisines"].nunique())

print("\nAverage Rating:", round(clean_df["rate"].mean(), 2))

print("Average Votes:", round(clean_df["votes"].mean(), 2))

print("Average Cost for Two:", round(clean_df["approx_cost"].mean(), 2))


# In[93]:


print("\nRestaurant Types:")
print(clean_df["restaurant_type"].value_counts().head(10))

print("\nTop Locations:")
print(clean_df["location"].value_counts().head(10))

print("\nTop Cuisines:")
print(clean_df["cuisines"].value_counts().head(10))


# In[96]:


print("Average rating:", clean_df["rate"].mean())
print("Median rating:", clean_df["rate"].median())

print("\nOnline Order:")
print(clean_df.groupby("online_order")["rate"].agg(["count", "mean"]))

print("\nTable Booking:")
print(clean_df.groupby("book_table")["rate"].agg(["count", "mean"]))

print("\nRestaurant Type:")
print(
    clean_df.groupby("restaurant_type")["rate"]
    .agg(["count", "mean"])
    .sort_values("count", ascending=False)
    .head(10)
)

print("\nLocation:")
print(
    clean_df.groupby("location")["rate"]
    .agg(["count", "mean"])
    .sort_values("count", ascending=False)
    .head(10)
)


# In[97]:


median_cost = clean_df["approx_cost"].median()

print("Median cost:", median_cost)


# In[98]:


clean_df["approx_cost"] = clean_df["approx_cost"].fillna(median_cost)


# In[99]:


print("Missing approx_cost:", clean_df["approx_cost"].isnull().sum())


# In[109]:


clean_df.to_csv(
    r"C:\Users\prajw\OneDrive\Documents\Zomato_project\cleaned_data.csv",
    index=False
)


# In[110]:


import os

file_path = r"C:\Users\prajw\OneDrive\Documents\Zomato_project\cleaned_data.csv"

print("File exists:", os.path.exists(file_path))
print("Saved at:", file_path)


# In[115]:


check_df = pd.read_csv(file_path)

print(check_df.shape)


# In[122]:


file_path = r"C:\Users\prajw\OneDrive\Documents\Zomato_project\cleaned_data.csv"

clean_df.to_csv(file_path, index=False)

print("DataFrame rows:", len(clean_df))
print("File saved to:", file_path)


# In[117]:


check_df = pd.read_csv(file_path)

print("CSV rows:", len(check_df))
print("CSV shape:", check_df.shape)


# In[120]:


print("Rows:", len(clean_df))

blank_rows = clean_df.isna().all(axis=1).sum()

print("Completely blank rows:", blank_rows)


# In[ ]:





# In[ ]:





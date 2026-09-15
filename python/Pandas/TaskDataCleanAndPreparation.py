import pandas as pd

data = {
    "car": ["Toyota", None, "Ford", "Chevrolet", "Chevrolet", "BMW"],
    "year": [2020, 2019, None, 2018, 2021, 2002]
}
df = pd.DataFrame(data)

# Create a DataFrame with at least one missing value and one duplicate row. 
# Use .isnull().sum() and .duplicated() to detect both before touching anything.
print(f'Empty in data:\n{df.isnull().sum()}')
print(f'Duplicates in data:\n{df.duplicated().sum()}')

# Handle the missing value two ways: once by dropping the row (dropna()), 
# once by filling it with the column average (fillna(mean))
# on two separate copies of the DataFrame, so you can compare.
df.dropna(subset=["car"], inplace=True)
print(f'After dropping empty rows in car column:\n{df}')

df_fill = df["year"].fillna(df["year"].mean(), inplace=True)
print(f'After filling empty values in year column:\n{df_fill}')

# 3. Remove the duplicate row using drop_duplicates().
df.drop_duplicates(subset=["car"], inplace=True)
print(f'After dropping duplicates:\n{df}')

# 4. Add a new engineered column using .apply(lambda x: ...) — 
# anything of your choosing (a category, a converted unit, a flag).
df["Age"] = df["year"].apply(lambda x: "New" if x > 2020 else "Old")
print(f'After adding Age column:\n{df}')

df_all_rows = df[df["year"] < 2020]
print(f'Rows with year < 2020:\n{df_all_rows}')

df_filter = df_all_rows[["car", "Age"]]
print(f'Filtered rows:\n{df_filter}')

print(f'Combined filtered:\n{df[df["year"] < 2020][["car", "Age"]]}')

test_data = {
    "test_name": ["test_login", "test_logout", "test_signup", "test_login", "test_checkout"],
    "status": ["Pass", "Fail", None, "Pass", "Pass"],
    "duration_ms": [120, 340, 95, 120, None]
}
df = pd.DataFrame(test_data)

# 1. Report how many missing values exist in each column
print(f'Missing values in each column:\n{df.isnull().sum()}')

# 2. Drop the duplicate row (test_login appears twice, identically)
df.drop_duplicates(subset=["test_name"], inplace=True)
print(f'After dropping duplicates:\n{df}')

df_fill = df.copy()
df_fill["duration_ms"] = df_fill["duration_ms"].fillna(df_fill["duration_ms"].mean())
df = df_fill[["test_name", "status", "duration_ms"]]
print(f'After filling missing duration_ms values:\n{df_fill}')

# 4. Fill missing "status" with the string "Unknown"
# Alternative type
df.fillna(value={
    "duration_ms": df["duration_ms"].mean(),
    "status": "Unknown"
}, inplace=True)
print(f'After filling missing duration_ms values:\n{df}')

df["is_slow"] = df["duration_ms"].apply(lambda x: True if x > 150 else False)
print(f'After adding is_slow column:\n{df}')

# set the index in data frame itself, and then reset it back to the default integer index.
df.set_index("test_name", inplace=True)
print(f'After setting index to test_name:\n{df}')

df.reset_index(drop=True, inplace=True)
print(f'After dropping index:\n{df}')

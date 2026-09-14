import numpy as np
import pandas as pd
import os

test_data = {
    "test_name": ["test_login", "test_logout", "test_signup", "test_checkout"],
    "status": ["Pass", "Fail", "Pass", "Fail"],
    "duration_ms": [120, 340, 95, 480]
}
df = pd.DataFrame(test_data)
print(df)

# 1. Print only the failed tests
# Now the outer df[...] takes that True/False Series from Step 2, 
# and uses it as a mask — keeping only the rows where the value was True, and dropping every row where it was False.
df_status_fail = df[df["status"] == "Fail"]
print(f'Tests with status \'Fail\': \n{df_status_fail}')

# 2. Sort by duration_ms, descending
df_sorted_duration = df.sort_values("duration_ms", inplace=False, ascending=False)
print(f'Tests sorted by duration (longest first): \n{df_sorted_duration}')

# 3. Group by status and print the average duration_ms per status
print(f'Total duration of all tests: {df["duration_ms"].sum()/df.shape[0]} ms')
df_status_group = df.groupby("status")["duration_ms"].mean()
print(f'Average duration of tests by status: \n{df_status_group}')

# 4. Save the DataFrame to a CSV file using df.to_csv("results.csv", index=False)
dir_name = os.path.dirname(os.path.abspath(__file__))
test_data_dir = os.path.join(dir_name, "..", "..", "Test_Data")
df_status_group.to_csv(f'{test_data_dir}\\Dataframes.csv', index=True) #index=False means don't write the index column to the file

# 5. Bonus: Group by status, and for each status, print the average duration_ms and a list of test_name values (as a single string, comma-separated). Save this to a new CSV file.
df_sorted = df.groupby("status").agg(
        average_duration_ms = ("duration_ms", "mean"),
        test_name = ("test_name", ",".join)
)

df_sorted.to_csv(f'{test_data_dir}\\Dataframes_sorted.csv', index=True) #index=False means don't write the index column to the file
print(f'Sorted test name: \n{df_sorted["test_name"]
                             .str.split(",")
                             .explode()
                             .str.strip()
                             .to_list()}')

# Geeting multiple columns from a DataFrame
df_multiple_columns = df[["test_name", "duration_ms"]]
print(f'Multiple columns from DataFrame: \n{df_multiple_columns}')

test_data2 = {
    "test_name": [None, "test_info"],
    "status": ["Fail", None],
    "duration_ms1": [np.nan, 200]
}
df2 = pd.DataFrame(test_data2)

df_merged = df.merge(df2, on="test_name", how="outer", suffixes=("_df1", "_df2"))
print(f'Merged DataFrame: \n{df_merged}')

print(f'Selected row by index:\n{df.iloc[0:1]}')
print(f'Selected row by label:\n{df.loc[1, "status"]}')
print(f'Selected row by label:\n{df.loc[0:1, ["status", "duration_ms"]]}')
print(f'Selected row by label:\n{df.loc[0:2, ["test_name", "status"]][df.loc[0:2, "status"] == "Fail"]}')

print(f'Empty cell value:\n {df_merged.isna().sum()}')
print(f'Is null value:\n {df_merged.isnull()}')
"""
Pandas Specification and Feature Demo

This file demonstrates the major pandas keywords, objects, and features with Python.
It is intended as a compact reference and runnable example for learning.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


# -----------------------------------------------------------
# 1. Core pandas objects and keywords
# -----------------------------------------------------------
# pandas.Series
# pandas.DataFrame
# pandas.Index
# pandas.MultiIndex
# pandas.Categorical
# pandas.Timestamp
# pandas.Timedelta
# pandas.date_range
# pandas.period_range
# pandas.read_csv
# pandas.read_excel
# pandas.merge
# pandas.concat
# pandas.concat(..., axis=1)
# pandas.melt
# pandas.pivot_table
# pandas.groupby
# pandas.resample
# pandas.apply
# pandas.map
# pandas.to_csv
# pandas.to_excel
# -----------------------------------------------------------


# -----------------------------------------------------------
# 2. Basic Series creation and operations
# -----------------------------------------------------------
def demo_series() -> None:
    s1 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'], name='values')
    s2 = pd.Series({'x': 5, 'y': 10, 'z': 15}, name='other')

    print("Series s1:\n", s1)
    print("\nSeries s2:\n", s2)
    print("\nSeries sum:\n", s1 + 5)
    print("\nSeries head:\n", s1.head(2))
    print("\nSeries describe:\n", s1.describe())


# -----------------------------------------------------------
# 3. Basic DataFrame creation and inspection
# -----------------------------------------------------------
def demo_dataframe() -> None:
    df = pd.DataFrame(
        {
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'City': ['New York', 'London', 'Paris'],
            'Salary': [50000, 65000, 70000],
        },
        index=['row1', 'row2', 'row3'],
    )

    print("\nDataFrame:\n", df)
    print("\nDataFrame shape:", df.shape)
    print("\nColumns:", list(df.columns))
    print("\nIndex:", df.index)
    print("\nDataFrame info:")
    df.info()


# -----------------------------------------------------------
# 4. Indexing, selecting, filtering
# -----------------------------------------------------------
def demo_indexing() -> None:
    df = pd.DataFrame(
        {
            'Name': ['Alice', 'Bob', 'Charlie', 'David'],
            'Age': [25, 30, 35, 40],
            'Score': [85, 90, 78, 88],
        },
        index=['r1', 'r2', 'r3', 'r4'],
    )

    print("\nSelecting single column:\n", df['Name'])
    print("\nSelecting rows by label with loc:\n", df.loc['r2':'r3'])
    print("\nSelecting rows by position with iloc:\n", df.iloc[1:3])
    print("\nFiltering rows with boolean mask:\n", df[df['Age'] >= 30])
    print("\nUnique values in Name:\n", df['Name'].unique())


# -----------------------------------------------------------
# 5. Missing values, duplicates, sorting, and renaming
# -----------------------------------------------------------
def demo_cleaning() -> None:
    df = pd.DataFrame(
        {
            'Name': ['Alice', 'Bob', 'Alice', None],
            'Age': [25, None, 25, 40],
            'Score': [90, 85, np.nan, 92],
        }
    )

    print("\nOriginal DataFrame:\n", df)
    print("\nMissing values count:\n", df.isna().sum())
    print("\nDrop rows with missing values:\n", df.dropna())
    print("\nFill missing values:\n", df.fillna({'Age': 0, 'Score': 0, 'Name': 'Unknown'}))
    print("\nDrop duplicate rows:\n", df.drop_duplicates())
    print("\nSort by Age:\n", df.sort_values('Age', na_position='last'))


# -----------------------------------------------------------
# 6. GroupBy, aggregation, pivot, and merge
# -----------------------------------------------------------
def demo_grouping_and_merge() -> None:
    sales = pd.DataFrame(
        {
            'Region': ['North', 'South', 'North', 'South'],
            'Product': ['A', 'A', 'B', 'B'],
            'Sales': [100, 200, 150, 250],
            'Units': [10, 15, 12, 16],
        }
    )

    print("\nSales DataFrame:\n", sales)
    print("\nGroupBy Region sum:\n", sales.groupby('Region').sum())
    print("\nGroupBy Region mean:\n", sales.groupby('Region')['Sales'].mean())

    pivot = sales.pivot_table(index='Region', columns='Product', values='Sales', aggfunc='sum')
    print("\nPivot table:\n", pivot)

    customers = pd.DataFrame(
        {
            'CustomerID': [1, 2, 3],
            'Name': ['Alice', 'Bob', 'Charlie'],
        }
    )

    orders = pd.DataFrame(
        {
            'OrderID': [101, 102, 103],
            'CustomerID': [1, 2, 4],
            'Amount': [50, 60, 70],
        }
    )

    merged = pd.merge(customers, orders, on='CustomerID', how='left')
    print("\nMerged DataFrame:\n", merged)


# -----------------------------------------------------------
# 7. Reshaping data using melt and concat
# -----------------------------------------------------------
def demo_reshape() -> None:
    df = pd.DataFrame(
        {
            'Date': ['2024-01-01', '2024-01-02'],
            'A': [10, 20],
            'B': [30, 40],
        }
    )

    print("\nOriginal dataframe:\n", df)
    melted = df.melt(id_vars='Date', var_name='Metric', value_name='Value')
    print("\nMelted dataframe:\n", melted)

    left = pd.DataFrame({'key': ['a', 'b'], 'value_left': [1, 2]})
    right = pd.DataFrame({'key': ['a', 'b'], 'value_right': [3, 4]})

    combined = pd.concat([left, right], axis=1)
    print("\nConcatenated dataframe:\n", combined)


# -----------------------------------------------------------
# 8. DateTime, Time Series, and resample
# -----------------------------------------------------------
def demo_timeseries() -> None:
    dates = pd.date_range(start='2024-01-01', periods=5, freq='D')
    ts = pd.Series(range(5), index=dates, name='daily_data')

    print("\nDate range:\n", dates)
    print("\nTime series:\n", ts)
    print("\nResample by week sum:\n", ts.resample('W').sum())


# -----------------------------------------------------------
# 9. Apply, map, and lambda usage
# -----------------------------------------------------------
def demo_apply_map() -> None:
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]})

    print("\nApply on column:\n", df['Age'].apply(lambda x: x + 1))
    print("\nMap example:\n", df['Name'].map({'Alice': 'A', 'Bob': 'B', 'Charlie': 'C'}))

    df['Category'] = df['Age'].apply(lambda x: 'Adult' if x >= 30 else 'Young')
    print("\nAfter apply to create category:\n", df)


# -----------------------------------------------------------
# 10. IO features: reading and writing CSV/Excel
# -----------------------------------------------------------
def demo_io() -> None:
    df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})

    df.to_csv('sample_data.csv', index=False)
    loaded = pd.read_csv('sample_data.csv')

    print("\nSaved and loaded CSV:\n", loaded)


# -----------------------------------------------------------
# 11. Categorical and MultiIndex examples
# -----------------------------------------------------------
def demo_categories_and_multiindex() -> None:
    df = pd.DataFrame(
        {
            'City': pd.Categorical(['NY', 'Paris', 'NY', 'Paris']),
            'Year': [2023, 2023, 2024, 2024],
            'Value': [10, 20, 30, 40],
        }
    )

    print("\nCategorical DataFrame:\n", df)

    mi = pd.MultiIndex.from_tuples([('A', 1), ('A', 2), ('B', 1)], names=['Group', 'ID'])
    print("\nMultiIndex:\n", mi)


# -----------------------------------------------------------
# 12. DataFrame methods summary (specification)
# -----------------------------------------------------------
def print_feature_summary() -> None:
    feature_list = [
        'Series',
        'DataFrame',
        'Index',
        'MultiIndex',
        'Categorical',
        'loc',
        'iloc',
        'groupby',
        'merge',
        'concat',
        'melt',
        'pivot_table',
        'sort_values',
        'dropna',
        'fillna',
        'to_csv',
        'read_csv',
        'to_excel',
        'read_excel',
        'apply',
        'map',
        'resample',
        'date_range',
        'Timestamp',
        'Timedelta',
    ]

    print("\nPandas features covered in this specification:")
    for item in feature_list:
        print('-', item)


# -----------------------------------------------------------
# 13. Main execution
# -----------------------------------------------------------
def main() -> None:
    print('Pandas version:', pd.__version__)
    print_feature_summary()
    demo_series()
    demo_dataframe()
    demo_indexing()
    demo_cleaning()
    demo_grouping_and_merge()
    demo_reshape()
    demo_timeseries()
    demo_apply_map()
    demo_io()
    demo_categories_and_multiindex()


if __name__ == '__main__':
    main()

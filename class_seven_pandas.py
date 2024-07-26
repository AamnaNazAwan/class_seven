# A series is a one dimensional labled array

import pandas as pd
#creating a series from a list
'''s = pd.Series([1, 3, 5, 7, 9])
#ACCESSING DATA BY POSITION
print(s)


#creating a series with custom index
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print(s)

#CREATING A SERIES FROM A DICTIONARY
s = pd.Series({'a':10, 'b':20, 'c':30})
print(s)

#ACCESSING DATA BY POSITION
print(s['a'])
#SLICING
print(s[:2])
print(s['a':'b'])

#OPERATION ON SERIES
s2 = pd.Series([1, 2, 3],
index = ['a', 'b', 'c'])
print(s + s2)

#APPLYING FUNCTIONS
print(s.apply(lambda x: x ** 2))


#STATISTICAL OPERATIONS
print(s.mean())
print(s.std())

# A Dataframe is a two dimensional ,size mutable (rows and columns)

#CREATING A DATAFRAME FRM DICTIONARY OF LISTS
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age' : [25,30,35],
    'City' : ['New York', 'Los Angles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)

#CREATING A DATAFRAME FROM A LISTS PF DICTIONARIES
data = [
    {'Name': 'Alice', 'Age':25, 'city': "newyork"},
    {'Name': 'Bob', 'Age':30, 'city': "Los Angeles"},
    {'Name': 'Charlie', 'Age': 35, 'city': "Chicago"}
]
df2 = pd.DataFrame(data)
print(df)

#CREATING A DATAFRAME FROM A NUMPY ARRAY
import numpy as np
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df = pd.DataFrame(data, columns=['A', 'B', 'C'])
print(df)

#ACCESSING A SINGLE COLUMN
print(df2['Name'])

#ACCESSING MULTIPLE COLUMNS
print(df2[['Name', 'city']])

#ACCESSING A ROW BY INDEX
print(df2.iloc[0]) # BY POSITION
print(df2.loc[1])  # BY LABEL

#SLICING ROWS
print(df2[1:3])


#OPERATIONS ON DATA FRAME
#ADDING A NEW COLUMN
df['salary'] = [50000, 6000, 34000]
print(df)
#DROPPING THE COLUMN
df.drop('salary', axis=1, inplace=True)
print(df)

#FILTERING ROWS
print(df[df['Age'] > 25])

#APPLYING FUNCTIONS
df['Age in 5 Years'] = df[ 'Age'].apply(lambda x: x + 5)
print(df)

#STATISTICAL OPERATIONS
print(df.describe())

#GROUPING AND AGGREGATION
grouped = df.groupby('age').mean()
print(grouped)

#ADVANCED DATAFRAME OPERATIONS
#MERGING DATA FRAME
df1 = pd.DataFrame({
    'key': ['A', 'B', 'C'],
    'value1': [1,2,3]
})
df2 = pd.DataFrame({
    'key': ['B', 'C', 'D'],
    'value2': [4,5,6]
})

df_merged = pd.merge(df1,df2, on='key', how='inner')
print(df_merged)

#PIVOT TABLE
data = {
    'Date':pd.date_range(start='2023-01-01', periods=6, freq='D'),
    'Category':['A','B','A','B','A','B'],
    'Value': [10,20,30,40,50,60]
}
df = pd.DataFrame(data)
pivot_table = df.pivot_table(values='Value', index='Date',
columns='Category')
print(pivot_table)

hourly_range = pd.date_range(start='23-01-01', periods=6,freq='h')
print(hourly_range)

data2 = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-02','2023-01-03','2023-01-04','2023-01-05'],
    'Product': ['Laptop', 'shirt', 'sofa', 'phone', 'pants'],
    'Category': ['Electronics', 'Clothing', 'Home', 'Electronics', 'Clothing'],
    'Quantity': [1,2,1,2,3],
    'Price': [1000, 20, 500, 800, 30]
})

data2['Total_sales'] = data2['Quantity'] * data2['Price']
#USING iloc TO SELECT THE FIRST 5 ROWS AND SPECIFIC COLUMNS
print(data2.iloc[:5, [1, 2, 5]])

#USING loc TO SELECT ROWS WHERE CATEGORY IS 'Electronics' AND SPECIFIC COLUMNS
print(data2.loc[data2['Category'] == 'Elecronics', ['Date', 'Product', 'Total_sales']])'''

#(STEP-1)CREATE A DATAFRAME
data = {
    'Date':pd.date_range(start='2023-01-01', periods=5, freq='D'),
    'Category':['A','B','A','B','A'],
    'Sales':[100,200,150,250,300]
}
df =pd.DataFrame(data)
print("iNITIAL dataframe")

#(STEP-2):Set 'Date' as the index
df.set_index('Date',inplace=True)
print("\nDataframe with 'Date' as index:")
print(df)
#(STEP-3) ACCESSING DATA USING LABELS
print("\nData for 2023-01-03:")
print(df.loc["2023-01-03"])

#(STEP-4)PERFORMING OPERATIONS WITH ALIGNMENT
df['Cumulative Sales'] = df['Sales'].cumsum()
print("\nDataFrame with cumulative sales:")
print(df)

#(STEP-5)GROUPING AND AGGREGATION
grouped = df.groupby('Category').sum()
print("\nTotal sales by category:")
print(grouped)


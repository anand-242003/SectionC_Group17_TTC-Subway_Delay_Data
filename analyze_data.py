import pandas as pd

df = pd.read_csv('Raw_dataset/Data.csv')

print('='*60)
print('DATASET OVERVIEW')
print('='*60)
print(f'Total Rows: {len(df)}')
print(f'Total Columns: {len(df.columns)}')
print(f'\nColumn Names and Types:')
print(df.dtypes)

print('\n' + '='*60)
print('BASIC STATISTICS')
print('='*60)
print(df.describe())

print('\n' + '='*60)
print('MISSING VALUES')
print('='*60)
missing = df.isnull().sum()
print(missing[missing > 0] if missing.sum() > 0 else 'No missing values')

print('\n' + '='*60)
print('UNIQUE VALUE COUNTS PER COLUMN')
print('='*60)
for col in df.columns:
    print(f'{col}: {df[col].nunique()} unique values')

print('\n' + '='*60)
print('SAMPLE DATA - First 5 rows')
print('='*60)
print(df.head())

print('\n' + '='*60)
print('VALUE COUNTS FOR KEY COLUMNS')
print('='*60)
print('\nDay distribution:')
print(df['Day'].value_counts())
print('\nLine distribution:')
print(df['Line'].value_counts())
print('\nBound distribution:')
print(df['Bound'].value_counts())

print('\n' + '='*60)
print('DELAY STATISTICS')
print('='*60)
print(f"Min Delay - Mean: {df['Min Delay'].mean():.2f}, Median: {df['Min Delay'].median():.2f}")
print(f"Min Delay - Max: {df['Min Delay'].max()}, Min: {df['Min Delay'].min()}")
print(f"Min Gap - Mean: {df['Min Gap'].mean():.2f}, Median: {df['Min Gap'].median():.2f}")
print(f"Min Gap - Max: {df['Min Gap'].max()}, Min: {df['Min Gap'].min()}")

print('\n' + '='*60)
print('TOP 10 STATIONS WITH MOST DELAYS')
print('='*60)
print(df['Station'].value_counts().head(10))

print('\n' + '='*60)
print('TOP 10 DELAY CODES')
print('='*60)
print(df['Code'].value_counts().head(10))

# Import pandas
import pandas as pd

# Import Twitter data as DataFrame: df
df = pd.read_csv(r'../Functions and Tuples/tweets.csv')


df2 = pd.read_csv(r'C:/Users/Mikele\/Desktop/Datacamp/digits.csv')

df3 = pd.read_csv(r'C:/Users/Mikele\/Desktop/Datacamp/titanic.csv')

print(df3.loc[[0], ['Sex']])
print(df3.loc[[0], ['Age']])
print(df3.iloc[[0], [5]])

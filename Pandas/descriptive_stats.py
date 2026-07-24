import pandas as pd

d = {
    'Name': pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack','Lee','David','Gasper','Betina','Andres']),
    'Age': pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
    'Rating': pd.Series([4.23,3.24,3.98,2.56,3.20,4.60,3.80,3.78,2.98,4.80,4.10,3.65])
}

df = pd.DataFrame(d)

print(df.sum(numeric_only=True))
print(df.mean(numeric_only=True))
print(df.std(numeric_only=True))
print(df.describe())
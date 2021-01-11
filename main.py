import pandas as pd

df1 = pd.read_excel("file_1.xlsx")
df2 = pd.read_excel("file_2.xlsx")

df3 = df1.merge(df2, on="cislo", how="inner")

print(df3)

import pandas as pd

df1 = pd.read_excel("file_1.xlsx")
df2 = pd.read_excel("file_2.xlsx")

df1.insert = (2, "data1")
df1.insert = (3, "data2")

for x in df1["cislo"]:
    for y in df2["cislo"]:
        if x == y:
            break


print(df1)
print(df2)

import pandas as pd

df = pd.read_csv("data.csv")

# 筛选含有2022年且countryName为中国的数据
data_2022_china = df[(df["updateTime"].str.contains("2022")) & (df["countryName"] == "中国")]

# 按provinceName分组，计算差值
grouped = data_2022_china.groupby("provinceName")
result = pd.DataFrame(columns=["provinceName", "province_confirmedCount"])

for name, group in grouped:
    first_count = group.iloc[0]["province_confirmedCount"]
    last_count = group.iloc[-1]["province_confirmedCount"]
    count_difference = first_count - last_count
    result = pd.concat([result, pd.DataFrame({"provinceName": [name], "province_confirmedCount": [count_difference]})])

# 输出结果
print(result)

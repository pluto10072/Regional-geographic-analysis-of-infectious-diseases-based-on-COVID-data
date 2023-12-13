import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data.csv")

# 筛选含有2022年且countryName为中国的数据
data_2022_china = df[(df["updateTime"].str.contains("2022")) & (df["countryName"] == "中国")]

# 按provinceName分组，计算差值
grouped = data_2022_china.groupby("provinceName")
result = pd.DataFrame(columns=["provinceName", "countDifference"])

for name, group in grouped:
    first_count = group.iloc[0]["province_confirmedCount"]
    last_count = group.iloc[-1]["province_confirmedCount"]
    count_difference = first_count - last_count
    result = pd.concat([result, pd.DataFrame({"provinceName": [name], "countDifference": [count_difference]})])


# 加载中国省级行政区划地图数据
china_map = gpd.read_file('map.json')

# 合并疫情数据和地图数据
merged_data = china_map.merge(result, left_on='name', right_on='provinceName')


# 绘制地理热力图
fig, ax = plt.subplots(figsize=(12, 8))
merged_data.plot(column='countDifference', cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# 设置图标题和坐标轴标签
plt.title('COVID-19 Confirmed Cases in China in 2022')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# 显示地理热力图
plt.show()



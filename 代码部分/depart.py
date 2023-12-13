import pandas as pd

df = pd.read_csv("data.csv")

yunnan = df[df["provinceName"] == "云南省"]
shanxi1 = df[df["provinceName"] == "陕西省"]
gansu = df[df["provinceName"] == "甘肃省"]
xinjiang = df[df["provinceName"] == "新疆维吾尔自治区"]
ningxia = df[df["provinceName"] == "宁夏回族自治区"]
guangdong = df[df["provinceName"] == "广东省"]
hunan = df[df["provinceName"] == "湖南省"]
hubei = df[df["provinceName"] == "湖北省"]
shandong = df[df["provinceName"] == "山东省"]
fujian = df[df["provinceName"] == "福建省"]
jiangsu = df[df["provinceName"] == "江苏省"]
heilongjiang = df[df["provinceName"] == "黑龙江省"]
liaoning = df[df["provinceName"] == "辽宁省"]
jilin = df[df["provinceName"] == "吉林省"]
neimeng = df[df["provinceName"] == "内蒙古自治区"]
shanxi2 = df[df["provinceName"] == "山西省"]
beijing = df[df["provinceName"] == "北京市"]
xizang = df[df["provinceName"] == "西藏自治区"]
jiangsu = df[df["provinceName"] == "江苏省"]
zhejiang = df[df["provinceName"] == "浙江省"]
hebei = df[df["provinceName"] == "河北省"]
fujain = df[df["provinceName"] == "福建省"]
shanghai = df[df["provinceName"] == "上海市"]
henan = df[df["provinceName"] == "河南省"]
guizhou = df[df["provinceName"] == "贵州省"]
tianjin = df[df["provinceName"] == "天津市"]
qinghai = df[df["provinceName"] == "青海省"]
anhui = df[df["provinceName"] == "安徽省"]
sichuan = df[df["provinceName"] == "四川省"]
hainan = df[df["provinceName"] == "海南省"]
chongqing = df[df["provinceName"] == "重庆市"]
guangxi = df[df["provinceName"] == "广西壮族自治区"]
xianggang = df[df["provinceName"] == "香港"]
aom = df[df["provinceName"] == "澳门"]

yunnan.to_csv("yunan_data.csv", index=False, encoding="utf-8-sig")
shanxi1.to_csv("shanxi1_data.csv", index=False, encoding="utf-8-sig")
gansu.to_csv("gansu_data.csv", index=False, encoding="utf-8-sig")
xinjiang.to_csv("xinjiang_data.csv", index=False, encoding="utf-8-sig")
ningxia.to_csv("ningxia_data.csv", index=False, encoding="utf-8-sig")
guangdong.to_csv("guangdong_data.csv", index=False, encoding="utf-8-sig")
hunan.to_csv("hunan_data.csv", index=False, encoding="utf-8-sig")
hubei.to_csv("hubei_data.csv", index=False, encoding="utf-8-sig")
shandong.to_csv("shandong_data.csv", index=False, encoding="utf-8-sig")
fujian.to_csv("fujian_data.csv", index=False, encoding="utf-8-sig")
jiangsu.to_csv("jiangsu_data.csv", index=False, encoding="utf-8-sig")
heilongjiang.to_csv("heilongjiang_data.csv", index=False, encoding="utf-8-sig")
liaoning.to_csv("liaoning_data.csv", index=False, encoding="utf-8-sig")
jilin.to_csv("jilin_data.csv", index=False, encoding="utf-8-sig")
neimeng.to_csv("neimeng_data.csv", index=False, encoding="utf-8-sig")
shanxi2.to_csv("shanxi2_data.csv", index=False, encoding="utf-8-sig")
beijing.to_csv("beijing_data.csv", index=False, encoding="utf-8-sig")
xizang.to_csv("xizang_data.csv", index=False, encoding="utf-8-sig")
zhejiang.to_csv("zhejiang_data.csv", index=False, encoding="utf-8-sig")
hebei.to_csv("hebei_data.csv", index=False, encoding="utf-8-sig")
fujian.to_csv("fujian_data.csv", index=False, encoding="utf-8-sig")
shanghai.to_csv("shanghai_data.csv", index=False, encoding="utf-8-sig")
henan.to_csv("henan_data.csv", index=False, encoding="utf-8-sig")
guizhou.to_csv("guizhou_data.csv", index=False, encoding="utf-8-sig")
tianjin.to_csv("tianjin_data.csv", index=False, encoding="utf-8-sig")
qinghai.to_csv("qinghai_data.csv", index=False, encoding="utf-8-sig")
anhui.to_csv("anhui_data.csv", index=False, encoding="utf-8-sig")
sichuan.to_csv("sichuan_data.csv", index=False, encoding="utf-8-sig")
hainan.to_csv("hainan_data.csv", index=False, encoding="utf-8-sig")
chongqing.to_csv("chongqing_data.csv", index=False, encoding="utf-8-sig")
guangxi.to_csv("guangxi_data.csv", index=False, encoding="utf-8-sig")
xianggang.to_csv("xianggang_data.csv", index=False, encoding="utf-8-sig")
aom.to_csv("aom_data.csv", index=False, encoding="utf-8-sig")

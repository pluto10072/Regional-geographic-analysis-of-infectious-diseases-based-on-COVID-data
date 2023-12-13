import requests
import requests

# 定义API的URL
url = "https://lab.isaaclin.cn/nCoV/api/rumors"

try:
    # 发送GET请求
    response = requests.get(url)

    # 检查响应状态码
    if response.status_code == 200:
        # 解析响应的JSON数据
        data = response.json()
        # 处理数据
        print(data)
    else:
        # 如果请求失败，打印错误信息
        print("请求失败，状态码：", response.status_code)
except requests.exceptions.RequestException as e:
    # 捕获请求异常
    print("请求发生异常：", e)

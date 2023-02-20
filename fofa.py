import requests
import json
import base64

# 填写 fofa 账号和 API 密钥
email = 'your_fofa_email'
key = 'your_fofa_api_key'

# 设置查询语句和页码范围
query = 'title="admin" && country="CN"'
start_page = 1
end_page = 3

# 定义函数用于获取 fofa 数据
def get_fofa_data(query, page):
    # 构造请求 URL
    url = f'https://fofa.so/api/v1/search/all?email={email}&key={key}&qbase64={base64.b64encode(query.encode()).decode()}&page={page}'
    # 发送 GET 请求获取数据
    response = requests.get(url)
    # 解析响应数据并返回
    return json.loads(response.text)

# 定义主函数用于批量爬取 fofa 数据
def main():
    # 循环遍历页码范围
    for page in range(start_page, end_page+1):
        # 获取当前页的 fofa 数据
        data = get_fofa_data(query, page)
        # 打印当前页的数据数量
        print(f'Page {page}: {len(data["results"])} results')
        # 循环遍历当前页的数据并打印
        for result in data['results']:
            print(result)

if __name__ == '__main__':
    main()

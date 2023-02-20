import argparse
import os
import sys
import requests
import socket
import whois
import nmap
from bs4 import BeautifulSoup

# ��������
parser = argparse.ArgumentParser(description='Information Gathering Script')
parser.add_argument('target', help='target domain or IP')
args = parser.parse_args()

# ��ʼ��
target = args.target
ip = socket.gethostbyname(target)
nm = nmap.PortScanner()

# ���banner��Ϣ
print('*' * 50)
print('Information Gathering Script'.center(50))
print('*' * 50)
print()

# ��ȡwhois��Ϣ
print('[+] Whois Information:')
w = whois.whois(target)
print(w.text)

# ��ȡIP��ַ��Ϣ
print('[+] IP Address Information:')
print(f'IP Address: {ip}')
r = requests.get(f'https://ipinfo.io/{ip}/json')
data = r.json()
for key in ['city', 'region', 'country', 'org']:
    print(f'{key.capitalize()}: {data[key]}')
print()

# �˿�ɨ��
print('[+] Port Scanning:')
nm.scan(ip, '1-1000')
for port in nm[ip]['tcp']:
    print(f'{port} {nm[ip]["tcp"][port]["name"]} {nm[ip]["tcp"][port]["state"]}')
print()

# ������Ϣй¶
print('[+] Sensitive Information Leakage:')
r = requests.get(f'http://{target}/robots.txt')
if r.status_code == 200:
    print('[!] robots.txt:')
    print(r.text)
print()

# ��ȡ��������Ϣ
print('[+] Subdomain Information:')
r = requests.get(f'https://crt.sh/?q=%.{target}&output=json')
data = r.json()
subdomains = set()
for item in data:
    subdomains.add(item['name_value'])
for subdomain in subdomains:
    print(subdomain)
print()

# ����
print('[+] Crawling:')
r = requests.get(f'http://{target}')
soup = BeautifulSoup(r.text, 'html.parser')
for link in soup.find_all('a'):
    href = link.get('href')
    if href is not None and target in href:
        print(href)
print()

# DNS��Ϣ�ռ�
print('[+] DNS Information:')
os.system(f'dig {target} ANY')
print()
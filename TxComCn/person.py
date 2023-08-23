import requests
import re

session = requests.Session()
session.get('https://tx.com.cn/space/cs/index.do?cf=hd')
with open('456456.txt', 'w', encoding='utf-8') as f:
    for page in range(1, 34):
        url = f'https://tx.com.cn/im/cs/default.do?page={page}&z=0iOcPKxjMk'
        res = session.get(url)

        patt = r'f=1">(.*?)</a>'
        names = re.findall(patt, res.text)
        
        for name in names:
            f.write(name + '\n')
        print(f'第{page}打印完毕')
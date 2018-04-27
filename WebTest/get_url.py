import os
import requests
from lxml import etree
from lxml import html
import openpyxl
import sys
import io

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
login_url="http://192.168.0.12/login.html"
res = requests.get(login_url)
#html_str = res.content.decode("utf-8")  # 通过content获得字节流进行转码，解决res.text获取中文显示乱码
#tree = etree.HTML(html_str)
#tt = tree.xpath("//input")
tree=html.fromstring(res.content)
print(tree)
tt= tree.findall(".//input")
for t in tt:
    print(t)
fo = open(r"C:\Users\admin\Desktop\log.txt", mode="w+", encoding="utf-8")
fo.write(res.content.decode("utf-8"))
fo.close()
# print(tree)

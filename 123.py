import urllib.request
import random
url='http://www.whatismyip.com.tw/'
iplist=['27.18.10.224:8998','121.232.6.96:8998','117.90.2.207:9000']
proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)})
opener=urllib.request.build_opener(proxy_support)
opener.addheasers=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.108 Safari/537.36')]
urllib.request.install_opener(opener)
response=urllib.request.urlopen(url)
html=response.read().decode('utf-8')
print(html)
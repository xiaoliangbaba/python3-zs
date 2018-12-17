__author__ = 'lilianga'

import urllib3

req = urllib3.Request("http://www.baidu.com")
response = urllib3.urlopen(req)
html = response.read()
print(html)

__author__ = 'lilianga'

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://quotes.toscrape.com"
response = urlopen(url)
# 初始化一个 bs 实例
#  对应的response对象的解析器， 最常用的解析方式，就是默认的  html.parser
bs = BeautifulSoup(response, "html.parser")

spans = bs.select("span.text")
list_quotes = []
for span in spans:
    span_text = span.text
    list_quotes.append(span_text.strip("“”"))
# 获取 10 个名言的作者
authors = bs.select("small")
list_authors = []
for author in authors:
    author_text = author.text
    list_authors.append(author_text)

# 获取这10个名言的  标签
divs = bs.select("div.tags")
list_tags = []
for div in divs:
    tag_text = div.select("a.tag")
    tag_list = [tag_a.text for tag_a in tag_text]
    list_tags.append(",".join(tag_list))

# 结果汇总
results = []
for i in range(len(list_quotes)):
    results.append("\t".join([list_quotes[i], list_authors[i], list_tags[i]]))

for result in results:
    print(result)

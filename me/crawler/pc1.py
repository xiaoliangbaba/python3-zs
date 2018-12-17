__author__ = 'lilianga'

from urllib.request import urlopen
import re


def spider_quotes():
    url = "http://quotes.toscrape.com"
    response = urlopen(url)
    html = response.read().decode("utf-8")

    #  获取 10  个  名言
    quotes = re.findall('<span class="text" itemprop="text">(.*)</span>', html)
    list_quotes = []
    for quote in quotes:
        #  strip 从两边开始搜寻，只要发现某个字符在当前这个方法的范围内，统统去掉
        list_quotes.append(quote.strip("“”"))

    # 获取 10 个名言的作者
    list_authors = []
    authors = re.findall('<small class="author" itemprop="author">(.*)</small>', html)
    for author in authors:
        list_authors.append(author)

    # 获取这10个名言的  标签
    tags = re.findall('<div class="tags">(.*?)</div>', html, re.RegexFlag.DOTALL)
    list_tags = []
    for tag in tags:
        temp_tags = re.findall('<a class="tag" href=".*">(.*)</a>', tag)
        tags_t1 = []
        for tag in temp_tags:
            tags_t1.append(tag)
            list_tags.append(",".join(tags_t1))

    # 结果汇总
    results = []
    for i in range(len(list_quotes)):
        results.append("\t".join([list_quotes[i], list_authors[i], list_tags[i]]))

    for result in results:
        print(result)


# 调取方法
spider_quotes()


import os
import requests
from urllib import request
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}

if not os.path.exists('./img'):
        os.mkdir('./img')
# for i in range(4):
#     if i == 1:
#         url = 'http://pic.netbian.com/4kmeinv/'
#     else:
#         url = 'http://pic.netbian.com/4kmeinv/index_%d.html' % i
#     response = requests.get(url, headers=headers)
#
#     page_text = response.text.encode('iso-8859-1').decode('gbk')
#     # print(page_text.encode('iso-8859-1').decode('gbk'))
#
#     tree = etree.HTML(page_text)
#     li_list = tree.xpath('//div[@class="slist"]/ul/li')
#     for li in li_list:
#         img_name = li.xpath('./a/b/text()')[0]
#         img_url = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
#         img_path = './img/' + img_name + '.jpg'
#         request.urlretrieve(img_url, img_path)
#         print(img_name, '下载成功！')
# print('全部完成!')


url = 'http://huaban.com/favorite/beauty/'
response = requests.get(url, headers=headers)
print(response.content)
# tree = etree.HTML(response.content)
# print(tree)
# img_list = tree.xpath('//div[@class="pin wfc"]')
# for img in img_list:
#     img_url = img.xpath('./a/img/@src')
#     print(img_url)

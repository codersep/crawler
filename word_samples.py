# 获取词典例句
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import string
from urllib.parse import quote
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def search_word_samples(word):
  url = 'http://dict.youdao.com/example/blng/'+ str(word) +'/#keyfrom=dict.main.moreblng'
  url = quote(url, safe=string.printable) # 解决编码问题
  # 模拟浏览器访问，绕过防爬虫机制
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
  ret = urlopen(Request(url, headers=headers)) #打开网站
  contents = ret.read() #读取网页
  soup = BeautifulSoup(contents, "html.parser")  #创建soup对象

  # 获取例句
  finalSample = []
  sample_group = []
  print('123')
  sp_lens = len(soup.select('ul[class="ol"] p'))
  if sp_lens > 24:
    sp_lens = 24
  for i in range(sp_lens):
    sp = soup.select('ul[class="ol"] p')[i].get_text()
    sample = " ".join(sp.split())
    sample_group.append(sample)


  sample_lens = int(len(sample_group) / 3)
  index = 0
  for i in range(sample_lens):
    finalSample.append([sample_group[index]]+[sample_group[index+1]]+[sample_group[index+2]])
    index = index + 3
  print(finalSample)
  return finalSample
if __name__ == "__main__":
    search_word_samples('test')
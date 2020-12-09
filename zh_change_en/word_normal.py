import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import string
from urllib.parse import quote
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


def zh_word_normal(word):
  url = 'http://dict.youdao.com/w/'+ str(word) +'/#keyfrom=dict2.index'
  url = quote(url, safe=string.printable) # 解决编码问题
  # 模拟浏览器访问，绕过防爬虫机制
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
  ret = urlopen(Request(url, headers=headers)) #打开网站
  contents = ret.read() #读取网页
  soup = BeautifulSoup(contents, "html.parser")  #实例化soup对象


  # ----------- 获取英文翻译
  wordGroups = []
  for i in range (len(soup.select('ul>p[class="wordGroup"]'))):
    wordGroup = soup.select('ul>p[class="wordGroup"]')[i].get_text()
    wordGroup = ''.join(wordGroup.split())
    wordGroups.append(wordGroup)

  # ------------- 获取短语
  final_phrase = []
  phrase_en = []
  phrase_zh = []

  for i in range(len(soup.select('div[id="webPhrase"]>p'))):
    phr_en = soup.select('div[id="webPhrase"] span')[i].get_text()
    phrase_en.append(phr_en)


  [s.extract() for s in soup('span')]  #过滤span标签
  # print(a)
  for i in range(len(soup.select('div[id="webPhrase"]>p'))):
    phr_zh = soup.select('div[id="webPhrase"] p')[i].get_text()
    zh = ''.join(phr_zh.split())
    phrase_zh.append(zh)

  for i in range(len(phrase_en)):
    final_phrase.append([phrase_en[i]]+[phrase_zh[i]])

  return [wordGroups,final_phrase]


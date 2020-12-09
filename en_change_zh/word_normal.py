import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import string
from urllib.parse import quote
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


def en_word_normal(word):
  url = 'http://dict.youdao.com/w/'+ str(word) +'/#keyfrom=dict2.index'
  url = quote(url, safe=string.printable) # 解决编码问题
  # 模拟浏览器访问，绕过防爬虫机制
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
  ret = urlopen(Request(url, headers=headers)) #打开网站
  contents = ret.read() #读取网页
  soup = BeautifulSoup(contents, "html.parser")  #实例化soup对象



  # --------------- 获取音标
  finalPhonetic = []
  for i in range(len(soup.select('span[class="pronounce"]'))):
    phonetic = soup.select('span[class="pronounce"]')[i].get_text()
    ptc = ":".join(phonetic.split())
    finalPhonetic.append(ptc)
  print(finalPhonetic)

# -------------- 获取译文
  finalMeaning = ''
  for i in range(len(soup.select('div[id="phrsListTab"] > div[class="trans-container"] > ul > li'))):
    meaning = soup.select('div[id="phrsListTab"] > div[class="trans-container"] > ul > li')[i].get_text()

    if i!=0:
      finalMeaning = finalMeaning + '\n' + meaning
    else:
      finalMeaning = meaning


# -------------- 获取单词表达形式：
  finalDistortion = ''
  if (soup.select('div[id="phrsListTab"] > div[class="trans-container"] > p')):  #判断是否存在p元素
    mode = soup.select('div[id="phrsListTab"] > div[class="trans-container"] > p')[0].get_text()
    finalDistortion = " ".join(mode.split())




  # ------------- 获取短语
  final_phrase = []
  phrase_en = []
  phrase_zh = []

  for i in range(len(soup.select('div[id="webPhrase"]>p'))):
    phr_en = soup.select('div[id="webPhrase"] span')[i].get_text()
    phrase_en.append(phr_en)
  # print(phrase_en)


  [s.extract() for s in soup('span')]  #过滤span标签
  # print(a)
  for i in range(len(soup.select('div[id="webPhrase"]>p'))):
    phr_zh = soup.select('div[id="webPhrase"] p')[i].get_text()
    zh = ''.join(phr_zh.split())
    phrase_zh.append(zh)

  for i in range(len(phrase_en)):
    final_phrase.append([phrase_en[i]]+[phrase_zh[i]])





  data = [finalPhonetic,finalMeaning,finalDistortion,final_phrase]
  return data

if __name__ == "__main__":
    en_word_normal('is')
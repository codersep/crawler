import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from crawler.test_word import isNull,isEnglish,isChinese
from crawler.en_change_zh.word_normal import en_word_normal
from crawler.zh_change_en.word_normal import zh_word_normal
from crawler.word_samples import search_word_samples


# -----------搜索标准格式单词音译
def searchNormal(word,ip):

  if isNull(word):
    print('用户: ' + ip + ' 非法操作')
    return {'code':500,'message':'非法字段'}
  else:
    if isEnglish(word):
      data = en_word_normal(word)
      final_data = {
      'code':200,
      'word': word,
      'Phonetic':data[0],
      'translation':data[1],
      'form':data[2],
      'phrase':data[3],
      }
      print('用户: ' + ip + ' 搜索了: ' + word)
      return final_data
    elif isChinese(word):
      data = zh_word_normal(word)
      final_data = {
        'code':200,
        'word':word,
        'wordGroups':data[0],
        'final_phrase':data[1]
      }
      print('用户: ' + ip + ' 搜索了: ' + word)
      return final_data
    else:
      data = {'code':500,'message':'非法字段'}
      print('用户: ' + ip + ' 非法操作')
      return data

# ----------- 搜索单词例句
def searchSamples(word,ip):
  if isNull(word):
    data = {'code':500,'message':'非法字段'}
    print('用户: ' + ip + ' 非法操作')
    return data
  else:
    if isEnglish(word) or isChinese(word):
      data = search_word_samples(word)
      final_data = {
        'code':200,
        'word':word,
        'samples':data
      }
      print('用户: ' + ip + ' 搜索了: ' + word)
      return final_data
    else:
      data = {'code':500,'message':'非法字段'}
      print('用户: ' + ip + ' 非法操作')
      return data


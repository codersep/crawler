import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import re

def isNull(word):
  if word.strip() == '':
    return True
  else:
    return False

def isChinese(word):
  for ch in word:
    if not'\u4e00' <= ch <= '\u9fa5':
        return False
  return True

def isEnglish(word):
  rule = re.compile(r"^[a-zA-Z.]{0,}$")
  mate_word = rule.match(word)
  if mate_word:
    return True
  else:
    return False
if __name__ == "__main__":
    print(isNull('123这'))
    print(isEnglish('123这'))
    print(isChinese('123这'))
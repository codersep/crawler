import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from crawler.search_word import searchSamples,searchNormal
from flask import Flask,request,jsonify
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
CORS(app,resources=r'/*')
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route('/dict/search/normal',methods=['GET'])
def get_normal():
  """
  获取单词标准信息接口
  """
  word = request.args.get('word')
  ip = request.remote_addr
  data = searchNormal(word,ip)
  return jsonify(data)

@app.route('/dict/search/samples',methods=['GET'])
def get_samples():
  """
  获取单词例句接口
  """
  word = request.args.get('word')
  ip = request.remote_addr
  data = searchSamples(word,ip)
  return jsonify(data)

if __name__ == "__main__":
    app.run()


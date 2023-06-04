from flask import Flask, request, Response
from threading import Thread
import requests as r
from bs4 import BeautifulSoup

app = Flask('')


@app.route('/favicon.ico')
def favicon():
  return Response(status=200)


@app.route('/', methods=['GET', 'POST'])
def handle_request():
  if request.method == 'POST':
    data = request.get_data(as_text=True)

    def insta(link):
      headers = {'accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-ch-ua-platform': "Windows", 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'}
      url = 'https://v3.saveinsta.app/api/ajaxSearch'
      data = {'q': link}
      a = r.post(url, data=data, headers = headers)
      b = a.text
      normal_text = b.encode('utf-8').decode('unicode_escape')
      soup = BeautifulSoup(normal_text, 'html.parser')
      anchor_tag = soup.find('a')
      link = anchor_tag['href']
      return link

    def douyin(lin):
      url = lin
      token = 'G7eRpMaa'
      u = f'https://dlpanda.com/'
      params = {'url': url, 'token': 'G7eRpMaa'}
      res = r.get(u, params=params)
      html = res.text
      soup = BeautifulSoup(res.text, 'html.parser')
      video_tag = soup.find('video')
      source_tag = video_tag.find('source')
      source_url = source_tag['src']
      return source_url

    if ('douyin' in data) or ("instagram" in data) or ('tiktok' in data):
      if 'douyin' in data or ('tiktok' in data):
        tuan = douyin(data)
      else:
        tuan = insta(data)
      return {"link": tuan, "author": "Le Tuan"}
    else:
      return 'You sent an unsupported link. Please check link'
  else:
    return 'API to download Instagram/Douyin/Tiktok video. Please use POST method with link. Developed by Le Tuan. Telegram Download Video: https://t.me/lhtvnbot'


def run():
  app.run(host='0.0.0.0', port=8080)


def keepalive():
  t = Thread(target=run)
  t.start()


keepalive()

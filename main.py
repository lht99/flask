from flask import Flask, request, Response
from threading import Thread
import requests as r
from bs4 import BeautifulSoup
import json
import base64
import time
import random
import re
from urllib.parse import unquote

app = Flask('')


@app.route('/robots.txt')
def robot():
  error = json.dumps({'message': "Nothing here!!!"})
  return Response(error, status=200, mimetype='application/json')


@app.route('/favicon.ico')
def favicon():
  error = json.dumps({'message': "Nothing here!!!"})
  return Response(error, status=200, mimetype='application/json')


@app.route('/', methods=['OPTIONS'])
def options():
  error = json.dumps({'message': "Nothing here!!!"})
  return Response(error, status=200, mimetype='application/json')


@app.route('/', methods=['GET', 'POST'])
def handle_request():
  if request.method == 'POST':
    data1 = request.args.to_dict(flat=True)
    for i in data1:
      if 'youtube' in str(i):
        k = i+'='+data1[i]
      else:
        k= i + data1[i]
    data = request.get_data(as_text=True)
    if len(data) == 0:
      data = k
    else:
      data = data
      if 'data=' in data:
        decoded_data = unquote(data).split('data=')[1]
        data = decoded_data

    def insta(link):
      url = 'https://v3.saveinsta.app/api/ajaxSearch'
      data = {'q': link}
      a = r.post(
        url,
        data=data,
        headers={
          'user-agent':
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57"
        }, timeout=10)
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
      tu = 0
      while tu == 0:
        res = r.get(
          u,
          params=params,
          headers={
            'user-agent':
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57"
          }, timeout=30)
        html = res.text
        soup = BeautifulSoup(res.text, 'html.parser')
        video_tag = soup.find('video')
        source_tag = video_tag.find('source')
        source_url = source_tag['src']
        tu = res.status_code
      return source_url

    def fb1(l):
      api = 'https://x2download.app/api/ajaxSearch/facebook'
      data = {'q': l, 'vt': 'facebook'}
      tu = 0
      while tu == 0:
        response1 = r.post(api, data=data, timeout=10)
        u = response1.status_code
        if u == 200 and response1.json()['links']:
          url = response1.json()['links']
          tu = u
          for key in url:
            if key == 'hd':
              link = url[key]
              break
            elif key == 'sd':
              link = url[key]
              break
            else:
              link = url[key]
        else:
          link = "Loi"
      return link

    def youtube(url):
      data = {'q': url, 'vt': 'home'}
      api = 'https://x2download.app/api/ajaxSearch'
      k = 0
      while k == 0:
        #time.sleep((random.randint(0, 1)))
        res = r.post(api, params=data, timeout=20)
        if res.status_code == 200 and res.json()['title']:
          js = res.json()
          title = js['title']
          js0 = js['links']['mp4']
          ma = []
          k = res.status_code
          for i in js0:
            ma.append(int(js0[i]['key']))
            maxx = max(ma)
            if js0[i]['key'] == str(maxx):
              quality = js0[i]['k']
            #quality = quality
      token = js['token']
      new = {
        'v_id': js['vid'],
        'ftype': 'mp4',
        'fquality': quality,
        'fname': title,
        'token': token,
        'timeExpire': js['timeExpires']
      }
      api2 = 'https://dt185.dlsnap11.xyz/api/json/convert'
      result = 0
      while result == 0:
        res2 = r.post(api2, params=new, timeout=30)
        #print(res2)
        js2 = res2.json()
        #print(js2)
        if js2['status'] == 'success' and js2['result'] != "Converting":
          url = js2['result']
          break
        else:
          continue
      return url

    if ('douyin' in data) or ("instagram" in data) or ('tiktok' in data):
      if 'douyin' in data or ('tiktok' in data):
        tuan = douyin(data)
      else:
        tuan = insta(data)
      error = json.dumps({
        'link': tuan,
        'contact': 'Le Tuan',
        'email': 'lht@duck.com',
        'author': 'Le Tuan',
        'tele': 'https://t.me/lhtvnbot', 'requested_url': data
      })
      return Response(error, status=200, mimetype='application/json')
    elif "facebook" in data or "fb.watch" in data:
      tuan = fb1(data)
      error = json.dumps({
        'link': tuan,
        'contact': 'Le Tuan',
        'email': 'lht@duck.com',
        'author': 'Le Tuan',
        'tele': 'https://t.me/lhtvnbot', 'requested_url': data
      })
      return Response(error, status=200, mimetype='application/json')
    elif ("youtube" in data) or ('youtu.be' in data):
      tuan = youtube(data)
      error = json.dumps({
        'link': tuan,
        'contact': 'Le Tuan',
        'email': 'lht@duck.com',
        'author': 'Le Tuan',
        'tele': 'https://t.me/lhtvnbot', 'requested_url': data
      })
      return Response(error, status=200, mimetype='application/json')
    else:
      return 'You sent an unsupported link. Please check link'
  else:
    a = r.get('https://tai-video.onrender.com/')  #ping bot
    if a.status_code == 405:
      #head = request.headers
      #print(head)
      print("BOT OK")
    else:
      print("BOT DOWN")
    error = json.dumps({
      'message':
      "API to download Instagram/Douyin/Tiktok/FB/Youtube video. Please use POST method with link in body Request",
      'contact':
      'Le Tuan',
      'email':
      'lht@duck.com',
      'author':
      'Le Tuan',
      'tele':
      'https://t.me/lhtvnbot',
      'supported':
      "Facebook, Douyin, Tiktok, Instagram, Youtube"
    })
    return Response(error, status=200, mimetype='application/json')


def run():
  app.run(host='0.0.0.0', port=8080)


def keepalive():
  t = Thread(target=run)
  t.start()


keepalive()

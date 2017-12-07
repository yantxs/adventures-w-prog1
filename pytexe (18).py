#Python 3.x, for Python 2.7 Twitter Client: http://pastebin.com/peP6nrhf
import urllib.request
import json


def busca_tweets(texto='python'):
  url = 'http://search.twitter.com/search.json?q=' + texto
  resp = urllib.request.urlopen(url).read()
  data = json.loads(resp.decode('utf-8'))
  return data['results']
 
 
def print_tweets(tweets):
  for t in tweets:
    print (t['from_user'] + ': ' + t['text'] + '\n')
 
resultados = busca_tweets('TDC2012')
print_tweets(resultados)

import requests
import json
import sys
import time
r = requests.get('https://etherchain.org/api/basic_stats').json()
def avg(l): return sum([i for i in l])/float(len(l))
blockTimeAvg = avg([int(b['blockTime']) for b in r['data']['blocks']])
difficultyAvg = avg([int(b['difficulty']) for b in r['data']['blocks']])
r = requests.get('http://coinmarketcap-nexuist.rhcloud.com/api/eth').json()
data = {
    'blockTime': blockTimeAvg,
    'difficulty': difficultyAvg,
    'priceUsd': float(r['price']['usd']),
    'lastUpdate': time.time(),
}
file(sys.argv[1], 'w').write('ethereumStats = ' + json.dumps(data) + ';')

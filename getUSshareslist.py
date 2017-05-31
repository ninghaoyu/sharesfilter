#!/usr/bin/python3

#from bs4 import BeautifulSoup
import socket,regex,os,json,sys
import urllib.request
from pyquery import PyQuery as pq

req_headers = {
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
	}
PAGES=139
BASEURL='https://xueqiu.com/S/?page=%s&exchange=US'
URLS=[ BASEURL.strip() % i for i in range(1,PAGES+1) ]


#print(URLS)

#os._exit(0)
allShares=[]

for url in URLS:
	reqobj = urllib.request.Request(url,headers=req_headers)
	req = urllib.request.urlopen(reqobj)
	htm_script=pq(req.read().decode('utf-8'))('script')
	m = regex.search('stockList.searchResult=(.*);',htm_script.text())
	#print(json.dumps(m[1],indent=4, separators=(',', ': ')))
	stocks = json.loads(m[1])
	#print(stocks["stocks"]["stocks"])
	#print(m[1])
	allShares += stocks["stocks"]["stocks"]

	#print(json.dumps(m[1], sys.stdout,sort_keys=True, indent=2))
	#json.dump(obj, outfile, sort_keys=sort_keys, indent=4)
	


print(allShares)


